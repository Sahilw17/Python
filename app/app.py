# pip install streamlit
# streamlit run .\app.py

import streamlit as st
import pandas as pd
from mock_data import mock_data
import time

with st.sidebar:
    st.title("Navigation", width="content")
    selection = st.sidebar.radio("Select Option", ["💬 Chat", "📚 Knowledge Base"])
    if selection == "💬 Chat":
        st.set_page_config(page_title="Streamlit Web UI Implementation", page_icon="🤖", layout="centered")

    if selection == "📚 Knowledge Base":
        st.set_page_config(page_title="Streamlit Web UI Implementation", page_icon="🤖", layout="wide")
        st.text_input(label="", placeholder="🔍 Search Knowledge Hub")
        with st.expander("📁 SYS.2", expanded=False):
            if st.button("📄 Best Practices in Medication History Management"):
                st.session_state.selected_doc = "Best Practices in Medication History Management"

            if st.button("📄 A Guide to Efficient Clinical Documentation"):
                st.session_state.selected_doc = "A Guide to Efficient Clinical Documentation"

            if st.button("📄 Standards for Managing Patient Problem Lists"):
                st.session_state.selected_doc = "Standards for Managing Patient Problem Lists"

        with st.expander("📁 SYS.3"):
            if st.button("📄 Protocols for Medication Reconciliation"):
                st.session_state.selected_doc ="Protocols for Medication Reconciliation"
            
        with st.expander("📁 SWE.1", expanded=False):
            if st.button("📄 Vital Signs Monitoring Integration and Alerting"):
                st.session_state.selected_doc ="Vital Signs Monitoring Integration and Alerting"


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
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if selection == "💬 Chat":
    prompt = st.chat_input("Enter Requirement or Azure ID")

    if prompt and prompt != st.session_state.last_prompt:
        st.session_state.last_prompt = prompt 
        st.session_state.current_prompt = prompt
        st.session_state.response = ""

        with st.spinner("Generating user stories..."):
            time.sleep(2)
            # st.success("Done!")

            for row in mock_data:
                if row['requirement'] == prompt:
                    st.session_state.response = row["output"]
                    break
                else:
                    st.session_state.response = "No matching requirement found."

    # Show response only if present
    if st.session_state.current_prompt and st.session_state.response:
        with st.chat_message("user"):
            st.markdown(f"**{st.session_state.current_prompt}**")

        with st.chat_message("assistant"):
            st.markdown(st.session_state.response)
            label = "✍️ Write to Azure DevOps"
            disabled = False
            if st.session_state.get("write_clicked", False):
                label = "✅ Sent!"
                st.session_state.write_clicked = False
                disabled = True

            col1, col2, col3 = st.columns([0.1, 0.1, 1])
            with col1:
                st.button("👍", key=f'up_{st.session_state.current_prompt}')
            with col2:
                st.button("👎", key=f'down_{st.session_state.current_prompt}')
            with col3:
                if st.button(label, key=f'write_{st.session_state.current_prompt}', disabled=disabled):
                    st.session_state.write_clicked = True

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