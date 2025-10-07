import os
import re
import json
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_questions_from_content(text: str, num_questions: int = 20):
    """
    Generate exam-style questions from content text using Gemini.
    Returns a list of questions in the same format as parse_questions_from_text.
    """
    prompt = f"""
    You are an AI assistant that generates exam-style questions from content text.
    Create {num_questions} questions, including a mix of:
      - Multiple-choice questions
      - Fill-in-the-blank questions
      - Short-answer questions
    Use the EXACT JSON format:

    [
      {{
        "type": "multiple_choice" | "fill_blank" | "short_answer",
        "question": "string (if fill_blank, include blanks as ___ directly in text)",
        "options": ["A", "B", "C", "D"] (only if multiple_choice),
        "answer": "string"
      }}
    ]

    Text to generate questions from:
    {text[:15000]}
    """

    response = model.generate_content(prompt)

    match = re.search(r'\[.*\]', response.text, re.DOTALL)
    if not match:
        raise ValueError("Gemini did not return valid JSON.")

    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON structure from Gemini.")

