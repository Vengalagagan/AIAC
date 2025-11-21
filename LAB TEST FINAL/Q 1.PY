"""
Clinical Note Summarizer Module

This module provides functionality to convert long doctor notes into
short structured summaries using prompt engineering techniques.
"""
import sys


def summarize_clinical_notes(doctor_notes: str) -> dict:
    """
    Convert long doctor notes into a structured clinical summary.
    
    Args:
        doctor_notes (str): The full doctor's clinical notes to summarize.
        
    Returns:
        dict: A structured summary containing:
            - 'chief_complaint': Main reason for visit
            - 'diagnosis': Primary diagnosis
            - 'treatment': Recommended treatment plan
            - 'follow_up': Follow-up instructions
    
    Example:
        >>> notes = "Patient came in with severe headache..."
        >>> result = summarize_clinical_notes(notes)
        >>> print(result['chief_complaint'])
    """
    
    # Construct the prompt using prompt engineering best practices
    prompt = f"""Analyze the following doctor's notes and provide a structured summary.
Return the summary in this exact format:

CHIEF COMPLAINT: [one-line summary of main reason for visit]
DIAGNOSIS: [primary diagnosis]
TREATMENT: [brief treatment plan]
FOLLOW-UP: [follow-up instructions]

Doctor's Notes:
{doctor_notes}

Provide concise, medically accurate summaries."""

    # Mock AI model call (replace with actual API in production)
    summary_text = _mock_ai_call(prompt)
    
    # Parse the structured response into a dictionary
    parsed_summary = _parse_summary(summary_text)
    
    return parsed_summary


def _mock_ai_call(prompt: str) -> str:
    """
    Mock function simulating an AI API call.
    In production, replace with actual LLM API (OpenAI, Azure, etc.)
    
    Args:
        prompt (str): The prompt to send to the AI model.
        
    Returns:
        str: Simulated AI response.
    """
    # Placeholder for actual API call
    return """CHIEF COMPLAINT: Persistent headache and fever
DIAGNOSIS: Migraine with viral infection
TREATMENT: Prescribed paracetamol 500mg, rest, and hydration
FOLLOW-UP: Return in 3 days if symptoms persist"""


def _parse_summary(summary_text: str) -> dict:
    """
    Parse the AI-generated summary into a structured dictionary.
    
    Args:
        summary_text (str): Raw summary text from AI model.
        
    Returns:
        dict: Parsed summary with keys for each section.
    """
    parsed = {}
    lines = summary_text.strip().split('\n')
    
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().lower().replace(' ', '_')
            parsed[key] = value.strip()
    
    return parsed


# Test Cases
if __name__ == "__main__":
    # Interactive mode: accept multiline user input for doctor's notes
    print("Enter doctor's notes. End input with a blank line (press Enter twice).")
    print("Or type 'TEST' on a line by itself to run built-in test cases.")

    # Read multiline input from the user until a blank line is entered after content
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        # If the user types a single line 'TEST', run the tests
        if not lines and line.strip().lower() == "test":
            run_tests = True
            break
        if line.strip() == "":
            if lines:
                break
            else:
                # ignore leading blank lines
                continue
        lines.append(line)

    # If user requested tests, run existing test cases
    if 'run_tests' in locals() and run_tests:
        # Test Case 1: Headache and fever
        print("Test Case 1: Headache and Fever")
        notes_1 = """Patient presented with severe headache and high fever for 3 days.
    Vital signs show temperature at 101.5°F. Physical examination reveals 
    throat redness. Patient reports fatigue and body aches. Prescribed 
    paracetamol and advised rest."""
        result_1 = summarize_clinical_notes(notes_1)
        print(result_1)
        print()

        # Test Case 2: Diabetes follow-up
        print("Test Case 2: Diabetes Follow-Up")
        notes_2 = """45-year-old patient with Type 2 diabetes comes for routine checkup.
    Blood sugar levels are within acceptable range. Weight has increased by 5 lbs.
    Patient reports occasional fatigue. Recommended increased physical activity
    and dietary modifications. Continue current medication."""
        result_2 = summarize_clinical_notes(notes_2)
        print(result_2)
        print()

        # Test Case 3: Ankle injury
        print("Test Case 3: Ankle Injury")
        notes_3 = """Patient injured left ankle during sports. Mild swelling and bruising observed.
    X-ray shows no fractures. Advised RICE protocol (Rest, Ice, Compression, Elevation).
    Prescribed anti-inflammatory medication. Patient cleared for light activities."""
        result_3 = summarize_clinical_notes(notes_3)
        print(result_3)
    else:
        # Process user-provided notes
        doctor_notes = "\n".join(lines).strip()
        if not doctor_notes:
            print("No notes provided. Exiting.")
            sys.exit(0)
        result = summarize_clinical_notes(doctor_notes)
        print("\nStructured Summary:")
        for k, v in result.items():
            print(f"{k}: {v}")