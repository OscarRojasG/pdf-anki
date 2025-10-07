import os
import re
import json
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

def parse_questions_from_text(text: str):
    """
    Parse questions (multiple choice, fill blank, short answer) from text using Gemini.
    Returns a list of question dicts.
    """
    prompt = f'''
    You are parsing exam-style questions from a PDF. The text may contain:
    - Multiple-choice questions
    - Fill-in-the-blank questions
    - Short-answer questions
    

    Return ONLY a valid JSON array, with each object in the format:
    {{
      "type": "multiple_choice" | "fill_blank" | "short_answer",
      "question": "string (if fill_blank, include blanks as ___ directly in text)",
      "options": ["A", "B", "C", "D"] (only if multiple_choice),
      "answer": "string",
      "feedback": "string",
    }}

    Text to analyze:
    {text[:15000]}
    '''
    response = model.generate_content(prompt)

    match = re.search(r'\[.*\]', response.text, re.DOTALL)
    if not match:
        raise ValueError("Gemini did not return valid JSON.")

    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON structure from Gemini.")

