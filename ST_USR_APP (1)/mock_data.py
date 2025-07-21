mock_data = [
    {
        "requirement": "Physicians need to quickly access a patient's complete medication history including current prescriptions, discontinued medications, allergies, and adverse drug reactions during patient encounters.",
        "output": """
**User Story 1:**
As a physician, I want to view a patient's current active medications with dosages and prescribing details, so that I can understand their current treatment regimen during clinical encounters.

**Acceptance Criteria:**
- **Scenario 1: Viewing active medications list**
  - Given a patient has active medications in their profile
  - When I access the patient's medication history
  - Then I should see a list of all current active medications
  - And each medication should display drug name, dosage, and frequency
  - And each medication should show prescribing physician and start date
  - And medications should be sorted by most recently prescribed first

- **Scenario 2: Viewing medications with no active prescriptions**
  - Given a patient has no active medications
  - When I access the patient's medication history
  - Then I should see a clear message indicating no active medications
  - And I should still be able to access other medication history sections

- **Scenario 3: Viewing medications with missing information**
  - Given some active medications have incomplete data
  - When I access the patient's medication history
  - Then medications with missing information should be clearly marked
  - And available information should still be displayed
  - And I should see indicators for missing data fields

**User Story 2:**
As a physician, I want to view a patient's discontinued medications with stop dates and reasons, so that I can understand their medication history and avoid prescribing previously problematic drugs.

**Acceptance Criteria:**
- **Scenario 1: Viewing discontinued medications**
  - Given a patient has discontinued medications in their history
  - When I access the discontinued medications section
  - Then I should see all previously prescribed medications that are no longer active
  - And each medication should display the stop date and reason for discontinuation
  - And I should see which physician discontinued each medication

- **Scenario 2: Filtering discontinued medications by time period**
  - Given a patient has extensive medication history
  - When I apply date filters to discontinued medications
  - Then I should see only medications discontinued within the selected time range
  - And I should be able to clear filters to view all discontinued medications

**User Story 3:**
As a physician, I want to view a patient's documented allergies with reaction details and severity levels, so that I can avoid prescribing medications that could cause allergic reactions.

**Acceptance Criteria:**
- **Scenario 1: Viewing patient allergies**
  - Given a patient has documented allergies in their profile
  - When I access the patient's allergy information
  - Then I should see all documented allergies with allergen names
  - And each allergy should display reaction type and severity level
  - And allergies should be color-coded by severity (red for severe, yellow for moderate)

- **Scenario 2: Viewing patient with no known allergies**
  - Given a patient has no documented allergies
  - When I access the allergy information
  - Then I should see a clear indication of 'No Known Allergies'
  - And I should be able to add new allergy information if needed

**User Story 4:**
As a physician, I want to view a patient's documented adverse drug reactions with clinical details, so that I can avoid prescribing medications that have previously caused adverse effects.

**Acceptance Criteria:**
- **Scenario 1: Viewing adverse drug reactions**
  - Given a patient has documented adverse drug reactions
  - When I access the adverse reactions section
  - Then I should see all documented reactions with medication names
  - And each reaction should display specific adverse effects and documentation date
  - And I should see clinical outcomes and treatments provided

- **Scenario 2: Viewing detailed reaction information**
  - Given I need more details about a specific adverse reaction
  - When I select a reaction from the list
  - Then I should see detailed clinical notes and timeline
  - And I should see any follow-up actions taken
"""
    },
    {
        "requirement": "Healthcare providers need to document patient encounters efficiently using templates while ensuring clinical notes meet quality standards and regulatory compliance requirements.",
        "output": """
**User Story 1:**
As a healthcare provider, I want to select appropriate encounter templates based on visit type, so that I can start documentation with relevant structured fields.

**Acceptance Criteria:**
- **Scenario 1: Selecting encounter templates**
  - Given I am beginning to document a patient encounter
  - When I access the documentation system
  - Then I should see a list of available templates organized by encounter type
  - And I should be able to select templates specific to my specialty
  - And the selected template should load with relevant structured fields
  - And the template should auto-populate with existing patient data where appropriate

- **Scenario 2: Customizing template fields**
  - Given I have selected an encounter template
  - When I need to modify the template for specific patient needs
  - Then I should be able to add custom fields to the template
  - And I should be able to remove non-relevant sections
  - And my customizations should be saved for future similar encounters

- **Scenario 3: Template unavailability handling**
  - Given no specific template exists for my encounter type
  - When I search for templates
  - Then I should be able to use a generic encounter template
  - And I should be able to request a new template for future use

**User Story 2:**
As a healthcare provider, I want to use voice-to-text dictation for clinical documentation, so that I can document patient encounters efficiently without extensive typing.

**Acceptance Criteria:**
- **Scenario 1: Using voice dictation for documentation**
  - Given I am documenting a patient encounter
  - When I activate the voice-to-text feature
  - Then the system should accurately convert my speech to text
  - And the system should recognize medical terminology correctly
  - And I should be able to pause and resume dictation as needed
  - And I should be able to review and edit the dictated text before saving

- **Scenario 2: Handling voice recognition errors**
  - Given the voice recognition system makes errors
  - When I review the dictated text
  - Then I should see highlighted uncertain words
  - And I should be able to correct errors by re-dictating or manual editing
  - And the system should learn from my corrections for improved accuracy

**User Story 3:**
As a healthcare provider, I want to receive real-time quality feedback on my clinical documentation, so that I can ensure completeness and compliance before finalizing notes.

**Acceptance Criteria:**
- **Scenario 1: Receiving documentation quality feedback**
  - Given I am completing clinical documentation
  - When I save or finalize the encounter note
  - Then the system should provide a completeness score for the documentation
  - And I should receive alerts for any missing required elements
  - And the system should highlight areas needing improvement
  - And I should see compliance status for billing and meaningful use requirements

- **Scenario 2: Addressing quality issues**
  - Given the system identifies quality issues in my documentation
  - When I review the feedback
  - Then I should see specific recommendations for improvement
  - And I should be able to quickly navigate to sections needing attention
  - And the system should re-evaluate quality after I make corrections

**User Story 4:**
As a healthcare provider, I want to validate billing compliance during documentation, so that I can ensure proper reimbursement and avoid coding issues.

**Acceptance Criteria:**
- **Scenario 1: Real-time billing compliance checking**
  - Given I am documenting a billable encounter
  - When I complete required documentation sections
  - Then the system should validate compliance with billing requirements
  - And I should see suggested ICD-10 and CPT codes based on my documentation
  - And the system should alert me to insufficient documentation for billing levels

- **Scenario 2: Code suggestion and validation**
  - Given the system suggests billing codes
  - When I review the suggestions
  - Then I should see confidence scores for each suggested code
  - And I should be able to accept, modify, or reject suggested codes
  - And the system should explain the rationale for code suggestions
"""
    },
    {
        "requirement": "Clinical staff need to view and update a patient's problem list with active diagnoses, chronic conditions, and resolved issues while maintaining accurate ICD-10 coding and clinical context.",
        "output": """
**User Story 1:**
As a clinical provider, I want to view a patient's current active problem list with diagnoses and clinical context, so that I can understand their current medical conditions during clinical encounters.

**Acceptance Criteria:**
- **Scenario 1: Viewing active problem list**
  - Given a patient has active diagnoses in their problem list
  - When I access the patient's problem list
  - Then I should see all active diagnoses with ICD-10-CM codes
  - And each problem should display the onset date and clinical status
  - And problems should be organized by clinical priority and severity
  - And I should see which provider documented each problem

- **Scenario 2: Viewing problem list with no active diagnoses**
  - Given a patient has no active diagnoses
  - When I access the patient's problem list
  - Then I should see a clear message indicating no active problems
  - And I should be able to add new problems if needed
  - And I should still be able to view resolved problems if any exist

- **Scenario 3: Viewing detailed problem information**
  - Given I need more information about a specific problem
  - When I select a problem from the list
  - Then I should see detailed clinical context and notes
  - And I should see the complete history of updates to that problem
  - And I should see any related care plans or interventions

**User Story 2:**
As a clinical provider, I want to add a new diagnosis to a patient's problem list with appropriate ICD-10 coding, so that other providers can see my clinical assessments.

**Acceptance Criteria:**
- **Scenario 1: Adding new diagnosis to problem list**
  - Given I have diagnosed a new condition for a patient
  - When I add the diagnosis to the problem list
  - Then I should be able to search for and select the appropriate ICD-10-CM code
  - And I should be able to set the problem status as active
  - And I should be able to enter the onset date and clinical context notes
  - And the new problem should be saved with my provider identification

- **Scenario 2: Adding diagnosis with uncertain coding**
  - Given I am unsure about the exact ICD-10 code
  - When I search for diagnosis codes
  - Then the system should provide code suggestions based on my search terms
  - And I should see code descriptions and clinical criteria
  - And I should be able to mark the diagnosis for coding review if needed

- **Scenario 3: Adding duplicate or related diagnoses**
  - Given I attempt to add a diagnosis that may be duplicate or related
  - When I search for the ICD-10 code
  - Then the system should alert me to similar existing problems
  - And I should be able to choose to update existing problems instead
  - And I should be able to proceed with adding if clinically appropriate

**User Story 3:**
As a clinical provider, I want to mark problems as resolved with resolution date and clinical notes, so that the patient's problem list accurately reflects their current health status.

**Acceptance Criteria:**
- **Scenario 1: Resolving an active problem**
  - Given a patient has an active problem that has been resolved
  - When I update the problem status to resolved
  - Then I should be able to enter the resolution date
  - And I should be able to add clinical notes explaining the resolution
  - And the problem should move from active to resolved status
  - And the resolved problem should remain visible in the historical problem list

- **Scenario 2: Updating problem status and details**
  - Given I need to modify an existing problem's details
  - When I edit the problem information
  - Then I should be able to update the clinical status (stable, worsening, improving)
  - And I should be able to modify onset dates if more accurate information becomes available
  - And all changes should be tracked with timestamps and provider identification

**User Story 4:**
As a clinical provider, I want to receive clinical alerts and care recommendations based on active problems, so that I can provide appropriate ongoing care for chronic conditions.

**Acceptance Criteria:**
- **Scenario 1: Receiving problem-based clinical alerts**
  - Given a patient has active chronic conditions on their problem list
  - When I access the patient's chart
  - Then I should see relevant clinical alerts for overdue screenings or monitoring
  - And I should receive care recommendations specific to their active diagnoses
  - And alerts should be prioritized based on clinical importance and urgency
  - And I should be able to acknowledge alerts and document follow-up actions

- **Scenario 2: Managing alert preferences**
  - Given I receive clinical alerts based on problem lists
  - When I want to customize alert settings
  - Then I should be able to adjust alert frequency and types
  - And I should be able to suppress alerts for specific conditions when appropriate
  - And my preferences should be saved for future patient encounters

**User Story 5:**
As a clinical provider, I want to reconcile problem lists during care transitions, so that diagnoses remain accurate and complete across different care settings.

**Acceptance Criteria:**
- **Scenario 1: Problem list reconciliation during admission**
  - Given a patient is being admitted with an existing problem list
  - When I review their problems during admission
  - Then I should see their current problem list alongside admission diagnoses
  - And I should be able to confirm, modify, or resolve existing problems
  - And I should be able to add new problems identified during admission
  - And all reconciliation activities should be documented with timestamps

- **Scenario 2: Handling conflicting problem information**
  - Given there are discrepancies between different sources of problem information
  - When I perform problem list reconciliation
  - Then I should see highlighted conflicts between sources
  - And I should be able to choose authoritative information
  - And I should be able to document clinical reasoning for reconciliation decisions
"""
    },
    {
        "requirement": "Healthcare providers need to review and reconcile patient medications during care transitions including hospital admissions, discharges, and transfers between care settings.",
        "output": """
**User Story 1:**
As a healthcare provider, I want to compare a patient's home medications with admission orders, so that I can identify discrepancies and ensure medication safety during care transitions.

**Acceptance Criteria:**
- **Scenario 1: Comparing home medications with admission orders**
  - Given a patient is being admitted with a documented home medication list
  - When I access the medication reconciliation workflow
  - Then I should see the patient's home medications alongside admission orders
  - And discrepancies should be clearly highlighted with visual indicators
  - And I should be able to view medication details including dosages and frequencies
  - And I should be able to document reasons for any medication changes

- **Scenario 2: Handling incomplete home medication information**
  - Given a patient's home medication list is incomplete or unclear
  - When I begin medication reconciliation
  - Then I should be able to contact pharmacy or family for verification
  - And I should be able to mark medications as "unable to verify"
  - And I should be able to document attempts made to obtain complete information

- **Scenario 3: Reconciling medications with multiple sources**
  - Given medication information exists from multiple sources
  - When I perform reconciliation
  - Then I should see medications from all available sources (pharmacy, patient, family)
  - And I should be able to compare and validate information across sources
  - And I should be able to document which source provided the most reliable information

**User Story 2:**
As a healthcare provider, I want to compare inpatient medications with discharge prescriptions, so that I can ensure continuity of care and identify necessary medication changes.

**Acceptance Criteria:**
- **Scenario 1: Comparing inpatient medications with discharge prescriptions**
  - Given a patient is being discharged with new prescription orders
  - When I access the discharge medication reconciliation
  - Then I should see inpatient medications alongside discharge prescriptions
  - And I should see which medications are being continued, stopped, or modified
  - And changes should be clearly marked with explanations
  - And I should be able to generate a medication reconciliation summary for the patient

- **Scenario 2: Identifying medication therapy changes**
  - Given medications have been modified during the hospital stay
  - When I review discharge medications
  - Then I should see clear indications of dose changes, frequency modifications, or formulation changes
  - And I should see clinical rationale for each change
  - And I should be able to verify that changes are appropriate for home use

**User Story 3:**
As a healthcare provider, I want to document the clinical reasoning for medication changes during reconciliation, so that other providers understand the rationale for modifications.

**Acceptance Criteria:**
- **Scenario 1: Documenting medication reconciliation decisions**
  - Given I have identified medication discrepancies during reconciliation
  - When I make decisions about medication changes
  - Then I should be able to document the clinical reasoning for each change
  - And I should be able to categorize changes as intentional or unintentional
  - And my documentation should be timestamped and attributed to me
  - And the reconciliation should be marked as complete once all discrepancies are addressed

- **Scenario 2: Collaborative reconciliation documentation**
  - Given multiple providers are involved in medication reconciliation
  - When we review medication changes together
  - Then each provider should be able to add their clinical input
  - And the system should track all contributors to the reconciliation process
  - And we should be able to reach consensus on final medication decisions

**User Story 4:**
As a healthcare provider, I want to track medication reconciliation completion status, so that I can ensure all required reconciliation activities are completed before care transitions.

**Acceptance Criteria:**
- **Scenario 1: Monitoring reconciliation completion status**
  - Given medication reconciliation is required for care transitions
  - When I check reconciliation status
  - Then I should see clear indicators of completion status for each reconciliation type
  - And I should see which reconciliation activities are pending or overdue
  - And I should receive alerts for incomplete reconciliation requirements
  - And the system should prevent certain transitions until reconciliation is complete

- **Scenario 2: Tracking reconciliation quality metrics**
  - Given reconciliation activities have been completed
  - When I review reconciliation quality
  - Then I should see metrics on reconciliation timeliness and completeness
  - And I should see patterns of medication discrepancies for quality improvement
  - And I should be able to generate reports for regulatory compliance

**User Story 5:**
As a clinical pharmacist, I want to review and verify medication reconciliation decisions, so that I can optimize therapy and prevent medication errors during care transitions.

**Acceptance Criteria:**
- **Scenario 1: Pharmacist review of reconciliation decisions**
  - Given medication reconciliation has been completed by other providers
  - When I review the reconciliation as a pharmacist
  - Then I should see all medication changes with clinical rationale
  - And I should be able to provide additional clinical recommendations
  - And I should be able to flag potential drug interactions or therapeutic issues
  - And I should be able to approve or request modifications to the reconciliation

- **Scenario 2: Collaborative medication optimization**
  - Given I identify opportunities for medication optimization
  - When I make recommendations during reconciliation review
  - Then I should be able to suggest alternative medications or dosing
  - And I should be able to communicate recommendations to the prescribing provider
  - And I should be able to track whether my recommendations were accepted
"""
    },
    {
        "requirement": "Clinical staff need to access and update patient vital signs data efficiently during patient care with automatic trending, abnormal value alerts, and integration with clinical workflows.",
        "output": """
**User Story 1:**
As a clinical staff member, I want to manually enter patient vital signs with timestamps, so that I can document vital signs measurements taken during patient care.

**Acceptance Criteria:**
- **Scenario 1: Manual vital signs entry**
  - Given I have taken a patient's vital signs measurements
  - When I enter the vital signs into the system
  - Then I should be able to input temperature, blood pressure, pulse, and respiratory rate
  - And the system should automatically timestamp the entry
  - And I should be able to add notes about measurement conditions or patient position
  - And the system should validate entered values against reasonable ranges

- **Scenario 2: Batch vital signs entry**
  - Given I need to enter multiple sets of vital signs for the same patient
  - When I use the batch entry feature
  - Then I should be able to enter several time-stamped vital sign sets efficiently
  - And I should be able to copy previous values as starting points
  - And the system should maintain proper chronological ordering

- **Scenario 3: Correcting vital signs entries**
  - Given I need to correct a previously entered vital sign value
  - When I edit the vital signs entry
  - Then I should be able to modify the values with appropriate documentation
  - And the system should maintain an audit trail of changes
  - And I should be able to add reasoning for the correction

**User Story 2:**
As a clinical staff member, I want to view graphical trends of patient vital signs over time, so that I can assess patterns and identify changes in patient condition.

**Acceptance Criteria:**
- **Scenario 1: Viewing vital signs trends**
  - Given a patient has multiple vital signs measurements over time
  - When I access the vital signs trending view
  - Then I should see graphical displays of vital signs over selected time periods
  - And I should be able to select different time ranges for trend analysis
  - And I should be able to overlay different vital signs on the same graph
  - And significant changes should be visually highlighted on the trend graph

- **Scenario 2: Comparing vital signs across different time periods**
  - Given I want to compare vital signs from different time periods
  - When I use the comparison feature
  - Then I should be able to select multiple date ranges for side-by-side comparison
  - And I should see statistical summaries for each time period
  - And I should be able to identify trends and patterns across periods

- **Scenario 3: Exporting vital signs trend data**
  - Given I need to share vital signs trends with other providers
  - When I export the trend data
  - Then I should be able to generate printable reports with graphs
  - And I should be able to export data in standard formats for external analysis
  - And exported reports should include patient identification and time ranges

**User Story 3:**
As a clinical staff member, I want to receive alerts when patient vital signs are outside normal ranges, so that I can respond quickly to potentially concerning changes.

**Acceptance Criteria:**
- **Scenario 1: Receiving abnormal vital signs alerts**
  - Given a patient's vital signs are entered that exceed normal parameters
  - When the abnormal values are detected
  - Then I should receive an immediate alert notification
  - And the alert should specify which vital signs are abnormal
  - And the alert should show the current values compared to normal ranges
  - And I should be able to acknowledge the alert and document my response

- **Scenario 2: Customizing alert thresholds**
  - Given different patients may have different normal ranges
  - When I configure alert settings for a specific patient
  - Then I should be able to adjust normal ranges based on patient age and conditions
  - And I should be able to set custom thresholds for individual patients
  - And the system should use patient-specific thresholds for alert generation

- **Scenario 3: Managing alert escalation**
  - Given critical vital signs require immediate attention
  - When critical thresholds are exceeded
  - Then the system should escalate alerts through multiple channels
  - And I should see different alert levels based on severity
  - And unacknowledged critical alerts should escalate to supervisors

**User Story 4:**
As a clinical staff member, I want to integrate vital signs from medical devices automatically, so that I can reduce manual entry and ensure accuracy.

**Acceptance Criteria:**
- **Scenario 1: Automatic device data integration**
  - Given medical devices are connected to the vital signs system
  - When devices transmit vital signs data
  - Then the data should automatically populate in the patient's record
  - And I should see real-time updates from connected devices
  - And device connectivity status should be clearly indicated
  - And I should be able to verify and approve device readings before finalizing

- **Scenario 2: Handling device connectivity issues**
  - Given medical devices may lose connectivity
  - When device connection is interrupted
  - Then I should receive notifications about connectivity status
  - And I should be able to switch to manual entry mode
  - And the system should attempt to reconnect automatically
  - And I should see clear indicators of data source (device vs manual)

**User Story 5:**
As a clinical staff member, I want vital signs to integrate with clinical workflows and early warning systems, so that patient care is coordinated and responsive to vital signs changes.

**Acceptance Criteria:**
- **Scenario 1: Early warning score calculation**
  - Given vital signs are entered or updated
  - When the system calculates early warning scores
  - Then I should see current early warning scores based on vital signs combinations
  - And I should see how the score has changed over time
  - And I should receive alerts when early warning scores indicate patient deterioration
  - And the system should suggest appropriate clinical interventions

- **Scenario 2: Integration with care protocols**
  - Given vital signs indicate specific clinical conditions
  - When vital signs meet protocol criteria
  - Then the system should suggest relevant care protocols or order sets
  - And I should be able to initiate protocols directly from vital signs alerts
  - And protocol activation should be documented in the patient record

- **Scenario 3: Handoff communication integration**
  - Given vital signs are important for patient handoffs
  - When I prepare handoff communications
  - Then vital signs trends should be automatically included in handoff reports
  - And I should be able to highlight significant vital signs changes
  - And receiving providers should have access to current and trending vital signs data
"""
    }
]


