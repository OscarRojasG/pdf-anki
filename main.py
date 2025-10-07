from reader.pdf import extract_pdf_text
from parser import parse_questions_from_text
from deck import create_anki_deck

def main():
    pdf_path = "questions.pdf"
    text = extract_pdf_text(pdf_path)
    questions = parse_questions_from_text(text)
    create_anki_deck(questions, deck_name="PDF Questions", output_file="output.apkg")

if __name__ == "__main__":
    main()

