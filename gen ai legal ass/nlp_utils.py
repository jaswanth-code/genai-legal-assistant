import re
from docx import Document
from PyPDF2 import PdfReader
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def split_clauses(text):
    clauses = re.split(r'\n|(?<=\.)\s', text)
    return [c.strip() for c in clauses if c.strip()]
