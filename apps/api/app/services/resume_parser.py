import pdfplumber
import docx

def extract_text_from_pdf(file_path: str):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_path: str):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def parse_resume(file_path: str):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    if file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)

    return ""