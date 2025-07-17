import streamlit as st
from mock_data import mock_data
import time
import markdown
import requests
from requests.auth import HTTPBasicAuth
from base64 import b64encode
import re, json
from response import get_response

ORGANIZATION = "suhasadevops"
PROJECT = "Golden_TATA_ACE"
access_token = "4z0YXUEjAszpa5O30Zvp1jpvwWuWAF7OdbzXJwoV9XXSJBgWtD7uJQQJ99BCACAAAAAAAAAAAAASAZDO2dFZ"
req_id = "SREQ_001_00100000"
API_URL = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT}/_apis/wit/workitems/$"
# https://dev.azure.com/suhasadevops/Golden_TATA_ACE

# Initialize session state
if "current_prompt" not in st.session_state:
    st.session_state.current_prompt = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = ""
if "success_time" not in st.session_state:
    st.session_state.success_time = 0
if "selected_doc" not in st.session_state:
    st.session_state.selected_doc = ""
if 'write_clicked' not in st.session_state:
    st.session_state.write_clicked = False
if "isReqCreationError" not in st.session_state:
    st.session_state.isReqCreationError = False
if "isReqCreationErrorContent" not in st.session_state:
    st.session_state.isReqCreationErrorContent = ""

def markdown_to_html(md_text: str) -> str:
    # html = markdown.markdown(md_text, extensions=["extra", "nl2br"])
#     md_text = """
# **Acceptance Criteria:**
# **Scenario 1: Viewing active medications list**
#   - Given a patient has active medications in their profile
#   - When I access the patient's medication history
#   - Then I should see a list of all current active medications
#   - And each medication should display drug name, dosage, and frequency
#   - And each medication should show prescribing physician and start date
#   - And medications should be sorted by most recently prescribed first

# **Scenario 2: Viewing medications with no active prescriptions**
#   - Given a patient has no active medications
#   - When I access the patient's medication history
#   - Then I should see a clear message indicating no active medications
#   - And I should still be able to access other medication history sections

# **Scenario 3: Viewing medications with missing information**
#   - Given some active medications have incomplete data
#   - When I access the patient's medication history
#   - Then medications with missing information should be clearly marked
#   - And available information should still be displayed
#   - And I should see indicators for missing data fields
# """
    html = markdown.markdown(md_text, extensions=["extra", "nl2br"])
    return html

def extract_all_acceptance_criteria(text):
    # Matches all blocks starting with "Acceptance Criteria:" up to next "User Story" or end of string
    pattern = r"(?s)\*\*Acceptance Criteria:\*\*\s*(.*?)(?=(\*\*User Story \d+:|\Z))"
    # pattern = r"(?s)Acceptance Criteria:\s*(.*?)\s*(?=User Story \d+:|$)"

    matches = re.findall(pattern, text)
    criteria_blocks = []

    for match in matches:
        block = match[0].strip()
        criteria_blocks.append("<b>Acceptance Criteria:</b>\n" + block.strip())

    return criteria_blocks

def get_lines_below_user_story(text):
    lines = text.splitlines()
    result = []

    for i, line in enumerate(lines):
        if "User Story" in line and i + 1 < len(lines):
            result.append(lines[i + 1].strip())

    return result

def create_workitem(title, data):
    global PROJECT, ORGANIZATION, access_token
    try:
        workitemId = None
        if not title.isdigit():
            workitemId = getWorkitemFromTitle(title, ORGANIZATION, PROJECT, access_token)
        else:
            workitemId = int(title)

        if workitemId:
            print("Extracting user stories & criterias from the response !")
            result = get_lines_below_user_story(data)
            acceptance_criteria_list = extract_all_acceptance_criteria(data)

            print("User Stories & Acceptance Criteria Extracted !")
            print(result)
            print(acceptance_criteria_list)

            add_childs(workitemId, result, acceptance_criteria_list)
    except Exception as e:
        print(f"Error while checking if work item already exists: ", e)

def add_childs(parent_id, data, acceptance_criteria_list):
    for title , description in zip(data, acceptance_criteria_list):
        description = markdown_to_html(description)
        headers = {
            "Content-Type": "application/json-patch+json",
            "Authorization": f"Basic {b64encode((':' + access_token).encode()).decode()}"
        }

        url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT}/_apis/wit/workitems/$User%20Story?api-version=7.0"

        body = [
            {
                "op": "add",
                "path": "/fields/System.Title",
                "value": title
            },
            {
                "op": "add", 
                "path": "/fields/System.Description", 
                "value": description
            },
            {
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",  # Child -> Parent
                    "url": f"https://dev.azure.com/{ORGANIZATION}/_apis/wit/workItems/{parent_id}",
                    "attributes": {
                        "comment": "Linked to parent"
                    }
                }
            }
        ]
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            work_item = response.json()
            print(f"Child Work Item Created: ID = {work_item['id']}")
        else:
            print(f'Failed to create Child workitem : "{title}"')

def get_work_item(work_item_id):
    global access_token, ORGANIZATION
    url = f"https://dev.azure.com/{ORGANIZATION}/_apis/wit/workitems/{work_item_id}?api-version=7.1-preview.3"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, auth=HTTPBasicAuth("", access_token))

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 404:
        print(f"⚠️ Work item {work_item_id} not found.")
        return False

    else:
        raise Exception(f"❌ Failed to fetch work item {work_item_id}: {response.status_code} - {response.text}")

# def get_user_stories(mock_data, requirement_title):
#     for row in mock_data:
#         if row['requirement'] == requirement_title:
#             st.session_state.response = row["output"]
#             break
#         else:
#             st.session_state.response = "No matching requirement found."

def get_user_stories(mock_data, requirement_title):
    st.session_state.response = get_response(requirement_title)

def getWorkitemFromTitle(title: str, orgnization: str, project: str, accessToken: str) -> int:
    wiqlQuery = {
        "query": f"""
            SELECT [System.Id], [System.Title], [System.WorkItemType], [System.State]
            FROM WorkItems
            WHERE [System.TeamProject] = '{project}'
            AND [System.Title] CONTAINS '{title}'
        """
    }

    apiUrl = f"https://dev.azure.com/{orgnization}/{project}/_apis/wit/wiql?api-version=7.0"

    response = requests.post(
        apiUrl,
        auth=HTTPBasicAuth('', accessToken),
        headers={"Content-Type": "application/json"},
        data=json.dumps(wiqlQuery)
    )

    if response.status_code == 200:
        workItems = response.json().get('workItems', [])
        if workItems:
            return workItems[0].get('id')
        else:
            st.session_state.isReqCreationError = True
            st.session_state.isReqCreationErrorContent = "❌ No maching Requirement Found"
            return None
    else:
        print(f'Error : The requirement with title "{title}" does not exist or check your input parameters')
        st.session_state.isReqCreationError = True
        st.session_state.isReqCreationErrorContent = "❌ No maching Requirement Found"
        return None


with st.sidebar:
    with st.container():
        st.header("User Stories Generation", divider=True)

    st.title("Navigation", width="content")
    selection = st.sidebar.radio("Select Option", ["💬 Chat", "📚 Knowledge Base"])

    if selection == "💬 Chat":
        st.set_page_config(page_title="Streamlit Web UI Implementation", page_icon="🤖", layout="centered")

    if selection == "📚 Knowledge Base":
        st.set_page_config(page_title="Streamlit Web UI Implementation", page_icon="🤖", layout="wide")
        st.text_input(label="", placeholder="🔍 Search Knowledge Hub")
        with st.expander("📁 Medication History Management", expanded=False):
            if st.button("📄 Best Practices in Medication History Management"):
                st.session_state.selected_doc = "Best Practices in Medication History Management"

            if st.button("📄 A Guide to Efficient Clinical Documentation"):
                st.session_state.selected_doc = "A Guide to Efficient Clinical Documentation"

            if st.button("📄 Standards for Managing Patient Problem Lists"):
                st.session_state.selected_doc = "Standards for Managing Patient Problem Lists"

        with st.expander("📁 Medication Reconciliation"):
            if st.button("📄 Protocols for Medication Reconciliation"):
                st.session_state.selected_doc ="Protocols for Medication Reconciliation"
            
        with st.expander("📁 Integration and Alerting", expanded=False):
            if st.button("📄 Vital Signs Monitoring Integration and Alerting"):
                st.session_state.selected_doc ="Vital Signs Monitoring Integration and Alerting"

if selection == "💬 Chat":
    prompt = st.chat_input("Enter Requirement or Azure ID")

    if prompt and prompt != st.session_state.last_prompt:
        st.session_state.last_prompt = prompt 
        st.session_state.current_prompt = prompt
        st.session_state.response = ""

        with st.spinner("Generating user stories..."):
            time.sleep(2)
            if st.session_state.current_prompt.isdigit():
                response = get_work_item(int(st.session_state.current_prompt))
                if response:
                    fields = response.get("fields")
                    st.session_state.response = fields.get("System.Title")
                    get_user_stories(mock_data, st.session_state.response)
                else:
                    st.session_state.response = "Agent Response Lost!!"
            else:
                print("Current Prompt:", st.session_state.current_prompt)
                get_user_stories(mock_data, st.session_state.current_prompt)

    # Show response only if present
    if st.session_state.current_prompt and st.session_state.response:
        with st.chat_message("user"):
            st.markdown(f"**{st.session_state.current_prompt}**")

        with st.chat_message("assistant"):
            st.markdown(st.session_state.response)
            label = "✍️ Write to Azure DevOps"
            disabled = False
            if st.session_state.get("write_clicked", False):
                print("Button Clicked !!")
                create_workitem(title=st.session_state.current_prompt, data=st.session_state.response)
                if st.session_state.isReqCreationError:
                    label = st.session_state.isReqCreationErrorContent
                    st.session_state.isReqCreationError = False
                else:
                    label = "✅ Sent!"
                st.session_state.write_clicked = False
                disabled = True

            if "Agent Response Lost !!" not in st.session_state.response:
                col1, col3 = st.columns([0.1, 0.1])
                with col1:
                    if st.button(label, key=f'write_{st.session_state.current_prompt}', disabled=disabled):
                        st.session_state.write_clicked = True
    else:
        print("No response found")

elif selection == "📚 Knowledge Base":
    col1, spacer1, btn1, btn2 = st.columns([4, 0.1, 1, 1])
    with col1:
        st.markdown("### 📚 Knowledge Hub") 
    with btn1:
        st.button("📤 Upload", use_container_width=True)
    with btn2:
        st.button("➕ New Folder", use_container_width=True)
    
    if st.session_state.selected_doc:
        st.header(st.session_state.selected_doc, divider=True)
        if st.session_state.selected_doc == "Best Practices in Medication History Management":
            with open(f"{st.session_state.selected_doc}.txt", 'r') as f:
                st.markdown(f.read())
        elif st.session_state.selected_doc == "A Guide to Efficient Clinical Documentation":
            with open(f"{st.session_state.selected_doc}.txt", 'r') as f:
                st.markdown(f.read())
        elif st.session_state.selected_doc == "Standards for Managing Patient Problem Lists":
            with open(f"{st.session_state.selected_doc}.txt", 'r') as f:
                st.markdown(f.read())
        elif st.session_state.selected_doc == "Protocols for Medication Reconciliation":
            with open(f"{st.session_state.selected_doc}.txt", 'r') as f:
                st.markdown(f.read())
        elif st.session_state.selected_doc == "Vital Signs Monitoring Integration and Alerting":
            with open(f"{st.session_state.selected_doc}.txt", 'r') as f:
                st.markdown(f.read())
    else:
        st.header("Select Document To Preview", divider=True)
        st.markdown("No Document Selected.")