from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = "".join([p.extract_text() or "" for p in reader.pages])
    return text
