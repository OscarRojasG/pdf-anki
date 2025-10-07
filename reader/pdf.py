import fitz  # PyMuPDF

def extract_pdf_text(pdf_path: str) -> str:
    """Extract all text from a PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

