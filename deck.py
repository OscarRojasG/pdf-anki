import genanki

def create_anki_deck(questions: list, deck_name="Gemini PDF Quiz", output_file="output.apkg"):
    """Generate an Anki deck file from a list of parsed questions."""
    deck = genanki.Deck(2059400110, deck_name)
    model = genanki.Model(
        1607392319,
        'Gemini Model',
        fields=[{'name': 'Question'}, {'name': 'Answer'}],
        templates=[{
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        }],
    )

    for q in questions:
        q_type = q.get("type", "").lower()
        question_text = q.get("question", "").strip()
        answer = q.get("answer", "").strip()

        if q_type == "multiple_choice":
            options = q.get("options", [])
            if options:
                question_text += "<br><br>" + "<br>".join(options)

        elif q_type == "true_or_false":
            question_text += "<br><br>(True or False)"

        elif q_type == "fill_blank":
            question_text += "<br><br>Fill in the blank: ___"

        elif q_type == "short_answer":
            question_text += "<br><br>(Short answer)"

        answer += "<br><br>"
        answer += q.get("feedback", "").strip()

        note = genanki.Note(model=model, fields=[question_text, answer])
        deck.add_note(note)

    genanki.Package(deck).write_to_file(output_file)
    print(f"✅ Anki deck saved as {output_file}")

