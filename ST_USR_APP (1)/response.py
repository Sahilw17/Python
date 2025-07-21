import ollama
from typing import List
import re

SYSTEM_PROMPT = """You are an expert healthcare business analyst and requirements engineer specializing in creating comprehensive user stories and acceptance criteria for healthcare systems. Your expertise encompasses electronic health records (EHR), clinical workflows, patient care coordination, regulatory compliance, and healthcare interoperability standards.

**CORE METHODOLOGY:**
**INVEST Principle for User Stories:**
- **Independent**: Each user story must be self-contained and deliverable without dependencies on other stories
- **Negotiable**: Stories should allow for discussion and refinement of implementation details
- **Valuable**: Each story must provide clear, measurable business or clinical value to end users
- **Estimable**: Stories should be clear enough for development teams to estimate effort and complexity
- **Small**: Break down complex requirements into atomic, manageable stories that can be completed in one development iteration
- **Testable**: Each story must have clear, verifiable acceptance criteria that can be validated through testing

**3Cs Quality Framework:**
- **Clear**: User stories must use unambiguous language that all stakeholders can understand
- **Complete**: Include all necessary information for implementation without gaps or assumptions
- **Consistent**: Use standardized terminology, format, and structure across all stories

**HEALTHCARE DOMAIN EXPERTISE:**

Apply deep knowledge of:
- Clinical workflows and care processes (admission, treatment, discharge, follow-up)
- Healthcare regulatory requirements (HIPAA privacy, meaningful use, quality reporting)
- Patient safety protocols and risk management considerations
- Medical terminology and clinical decision-making processes
- Healthcare data standards (HL7 FHIR, ICD-10, SNOMED-CT, RxNorm, LOINC)
- Interoperability and care coordination across healthcare settings
- Provider roles and responsibilities (physicians, nurses, pharmacists, therapists, administrators)

**USER STORY FORMAT SPECIFICATION:**
Each user story must follow this exact structure:
"As a [specific healthcare role], I want [specific capability or feature], so that [clear clinical or business benefit]."

**Example User Story:**
**User Story 1:**
As a primary care physician, I want to view a patient's medication adherence data from connected pharmacy systems, so that I can identify non-adherence patterns and adjust treatment plans to improve patient outcomes.

**ACCEPTANCE CRITERIA SPECIFICATION:**
Use Gherkin format with Given/When/Then structure for all acceptance criteria. Each user story must include 3-4 scenarios covering:
1. **Normal/Happy Path**: Primary use case with expected workflow
2. **Edge Cases**: Alternative paths, boundary conditions, or exceptional circumstances
3. **Error Handling**: System behavior when things go wrong or data is missing
4. **Data Validation**: Ensuring data integrity, security, and compliance requirements

**Example Acceptance Criteria in Gherkin Format:**

Scenario 1: Viewing medication adherence data for compliant patient:
Given a patient has active prescriptions with pharmacy fill data
When I access the medication adherence dashboard
Then I should see a list of current medications with adherence percentages
And each medication should display last fill date and days supply remaining
And adherence rates should be color-coded (green >80%, yellow 60-80%, red <60%)
And I should see adherence trends over the past 6 months with graphical representation

Scenario 2: Handling patient with no pharmacy data:
Given a patient has no connected pharmacy data available
When I access the medication adherence dashboard
Then I should see a clear message indicating no pharmacy data is available
And I should be able to manually document adherence information
And I should see options to help patient connect their pharmacy for future monitoring

Scenario 3: Identifying medication adherence issues:
Given a patient has poor adherence rates (below 60%) for critical medications
When I view the adherence data
Then the system should highlight non-adherent medications with red indicators
And I should see potential reasons for non-adherence (cost, side effects, complexity)
And I should receive suggestions for adherence improvement interventions
And I should be able to document adherence counseling in the patient record

Scenario 4: Error handling for pharmacy system connectivity issues

Given the pharmacy data connection is temporarily unavailable
When I attempt to access medication adherence information
Then I should see a clear error message explaining the connectivity issue
And I should see the last successful data update timestamp
And I should be able to access previously cached adherence data
And I should receive notification when connectivity is restored

**OUTPUT REQUIREMENTS:**
**1. User Story Generation:**
- Create 3-5 atomic user stories that collectively address the full requirement
- Ensure each story represents independent, valuable functionality
- Use specific healthcare roles (not generic "user" or "provider")
- Focus on clinical and operational benefits

**2. Comprehensive Acceptance Criteria:**
- Provide 3-4 Gherkin scenarios per user story
- Cover normal operations, edge cases, error conditions, and data validation
- Include specific healthcare data elements and realistic clinical scenarios
- Address security, privacy, and compliance requirements where applicable
"""

def get_llm_response(messages: List):
        try:
            response = ollama.chat(
                model="llama3",
                messages=messages,
                options={
                    'temperature': 0.1,
                    'max_tokens': 2048,
                }
            )

            return response.message.content
        
        except Exception as e:
            print("Error in Getting Response from Agent:", e)



def get_response(req: str) -> str:
    
    messages =  [
        {"role": "system", "content": SYSTEM_PROMPT},
        # {"role": "user", "content": """ 
        # # Good Examples
        # ## Example 1
        # Requirement: Physicians need to quickly access a patient's complete medication history including current prescriptions, discontinued medications, allergies, and adverse drug reactions during patient encounters.
        # Output: **User Story 1:**\nAs a physician, I want to view a patient's current active medications with dosages and prescribing details, so that I can understand their current treatment regimen during clinical encounters.\n**Acceptance Criteria:**\n**Scenario 1: Viewing active medications list**\n- Given a patient has active medications in their profile\n- When I access the patient's medication history\n- Then I should see a list of all current active medications\n- And each medication should display drug name, dosage, and frequency\n- And each medication should show prescribing physician and start date\n- And medications should be sorted by most recently prescribed first\n**Scenario 2: Viewing medications with no active prescriptions**\n- Given a patient has no active medications\n- When I access the patient's medication history\n- Then I should see a clear message indicating no active m  edications\n- And I should still be able to access other medication history sections\n**Scenario 3: Viewing medications with missing information**\n- Given some active medications have incomplete data\n- When I access the patient's medication history\n- Then medications with missing information should be clearly marked\n- And available information should still be displayed\n- And I should see indicators for missing data fields\n**User Story 2:**\nAs a physician, I want to view a patient's discontinued medications with stop dates and reasons, so that I can understand their medication history and avoid prescribing previously problematic drugs.\n**Acceptance Criteria:**\n**Scenario 1: Viewing discontinued medications**\n- Given a patient has discontinued medications in their history\n- When I access the discontinued medications section\n- Then I should see all previously prescribed medications that are no longer active\n- And each medication should display the stop date and reason for discontinuation\n- And I should see which physician discontinued each medication\n**Scenario 2: Filtering discontinued medications by time period**\n- Given a patient has extensive medication history\n- When I apply date filters to discontinued medications\n- Then I should see only medications discontinued within the selected time range\n- And I should be able to clear filters to view all discontinued medications\n**User Story 3:**\nAs a physician, I want to view a patient's documented allergies with reaction details and severity levels, so that I can avoid prescribing medications that could cause allergic reactions.\n**Acceptance Criteria:**\n**Scenario 1: Viewing patient allergies**\n- Given a patient has documented allergies in their profile\n- When I access the patient's allergy information\n- Then I should see all documented allergies with allergen names\n- And each allergy should display reaction type and severity level\n- And allergies should be color-coded by severity (red for severe, yellow for moderate)\n**Scenario 2: Viewing patient with no known allergies**\n- Given a patient has no documented allergies\n- When I access the allergy information\n- Then I should see a clear indication of 'No Known Allergies'\n- And I should be able to add new allergy information if needed\n**User Story 4:**\nAs a physician, I want to view a patient's documented adverse drug reactions with clinical details, so that I can avoid prescribing medications that have previously caused adverse effects.\n**Acceptance Criteria:**\n**Scenario 1: Viewing adverse drug reactions**\n- Given a patient has documented adverse drug reactions\n- When I access the adverse reactions section\n- Then I should see all documented reactions with medication names\n- And each reaction should display specific adverse effects and documentation date\n- And I should see clinical outcomes and treatments provided\n**Scenario 2: Viewing detailed reaction information**\n- Given I need more details about a specific adverse reaction\n- When I select a reaction from the list\n- Then I should see detailed clinical notes and timeline\n- And I should see any follow-up actions taken.

        # ## Example 2
        # Requirement: Healthcare providers need to document patient encounters efficiently using templates while ensuring clinical notes meet quality standards and regulatory compliance requirements.
        # Output: **User Story 1:**\nAs a healthcare provider, I want to select appropriate encounter templates based on visit type, so that I can start documentation with relevant structured fields.\n**Acceptance Criteria:**\n**Scenario 1: Selecting encounter templates**\n- Given I am beginning to document a patient encounter\n- When I access the documentation system\n- Then I should see a list of available templates organized by encounter type\n- And I should be able to select templates specific to my specialty\n- And the selected template should load with relevant structured fields\n- And the template should auto-populate with existing patient data where appropriate\n**Scenario 2: Customizing template fields**\n- Given I have selected an encounter template\n- When I need to modify the template for specific patient needs\n- Then I should be able to add custom fields to the template\n- And I should be able to remove non-relevant sections\n- And my customizations should be saved for future similar encounters\n**Scenario 3: Template unavailability handling**\n- Given no specific template exists for my encounter type\n- When I search for templates\n- Then I should be able to use a generic encounter template\n- And I should be able to request a new template for future use\n**User Story 2:**\nAs a healthcare provider, I want to use voice-to-text dictation for clinical documentation, so that I can document patient encounters efficiently without extensive typing.\n**Acceptance Criteria:**\n**Scenario 1: Using voice dictation for documentation**\n- Given I am documenting a patient encounter\n- When I activate the voice-to-text feature\n- Then the system should accurately convert my speech to text\n- And the system should recognize medical terminology correctly\n- And I should be able to pause and resume dictation as needed\n- And I should be able to review and edit the dictated text before saving\n**Scenario 2: Handling voice recognition errors**\n- Given the voice recognition system makes errors\n- When I review the dictated text\n- Then I should see highlighted uncertain words\n- And I should be able to correct errors by re-dictating or manual editing\n- And the system should learn from my corrections for improved accuracy\n**User Story 3:**\nAs a healthcare provider, I want to receive real-time quality feedback on my clinical documentation, so that I can ensure completeness and compliance before finalizing notes.\n**Acceptance Criteria:**\n**Scenario 1: Receiving documentation quality feedback**\n- Given I am completing clinical documentation\n- When I save or finalize the encounter note\n- Then the system should provide a completeness score for the documentation\n- And I should receive alerts for any missing required elements\n- And the system should highlight areas needing improvement\n- And I should see compliance status for billing and meaningful use requirements\n**Scenario 2: Addressing quality issues**\n- Given the system identifies quality issues in my documentation\n- When I review the feedback\n- Then I should see specific recommendations for improvement\n- And I should be able to quickly navigate to sections needing attention\n- And the system should re-evaluate quality after I make corrections\n**User Story 4:**\nAs a healthcare provider, I want to validate billing compliance during documentation, so that I can ensure proper reimbursement and avoid coding issues.\n**Acceptance Criteria:**\n**Scenario 1: Real-time billing compliance checking**\n- Given I am documenting a billable encounter\n- When I complete required documentation sections\n- Then the system should validate compliance with billing requirements\n- And I should see suggested ICD-10 and CPT codes based on my documentation\n- And the system should alert me to insufficient documentation for billing levels\n**Scenario 2: Code suggestion and validation**\n- Given the system suggests billing codes\n- When I review the suggestions\n- Then I should see confidence scores for each suggested code\n- And I should be able to accept, modify, or reject suggested codes\n- And the system should explain the rationale for code suggestions
        # """},
        # {"role": "assistant", "content": "Got it. These examples help me understand better. I would take care of the INVEST criteria, ensuring that each user story is detailed, concrete, and testable with acceptance criteria following the Gherkin syntax. I would also ensure that the acceptance criteria are specific, measurable, and testable."},
        {"role": "user", "content": f"Create User Stories with acceptance criteria for the following requirement: {req}.\n Just give me the User Stories & its Acceptance Criteria in Gherkin syntax without any other summary or output validation information as that is not useful for me. Ensure the user stories are formatted like: **User Story 1:** [User Story]\n**Acceptance Criteria 1:** [Acceptance Criteria] & similarly for others."}


    ]

    response = get_llm_response(messages)
    final_response = re.sub(r'<[Tt][Hh][Ii][Nn][Kk]>.*?</[Tt][Hh][Ii][Nn][Kk]>', '', response, flags=re.DOTALL | re.IGNORECASE).strip()
    print("Response Generated!")

    return final_response