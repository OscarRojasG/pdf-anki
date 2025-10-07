from reader.pdf import extract_pdf_text
from question_gen import generate_questions_from_content
from deck import create_anki_deck

def main():
    pdf_path = "content.pdf"
    deck_name = "Generated Quiz Deck"
    output_file = "generated_output.apkg"

    # Step 1: Extract text from PDF
    content_text = extract_pdf_text(pdf_path)

    # Step 2: Generate questions from content
    questions = generate_questions_from_content(content_text, num_questions=20)

    # Step 3: Create Anki deck
    create_anki_deck(questions, deck_name=deck_name, output_file=output_file)

if __name__ == "__main__":
    main()

