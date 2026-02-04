import streamlit as st
from io import BytesIO
from fpdf import FPDF

# -------- IMPORT YOUR MODULES --------
from nlp_utils import extract_text_from_pdf, extract_text_from_docx, split_clauses
from risk_scoring import score_clause, overall_contract_risk


# -------- STREAMLIT CONFIG --------
st.set_page_config(page_title="GenAI Legal Assistant", layout="wide")
st.title("📜 GenAI-Powered Legal Assistant for SMEs")


# -------- HELPER FUNCTIONS --------
def is_likely_contract(text):
    keywords = [
        "agreement", "party", "parties", "hereby",
        "shall", "liability", "termination",
        "jurisdiction", "governing law", "indemnity"
    ]
    text = text.lower()
    return sum(1 for k in keywords if k in text) >= 3


def explain_clause_simple(clause):
    clause = clause.lower()

    if "termination" in clause:
        return "This clause explains how and when the agreement can be ended."
    if "payment" in clause or "fee" in clause:
        return "This clause describes payment obligations."
    if "confidential" in clause:
        return "This clause requires parties to keep information private."
    if "jurisdiction" in clause or "governing law" in clause:
        return "This clause defines which court or location will handle disputes."

    return "This clause defines general rights and obligations between the parties."


def sanitize_text_for_pdf(text):
    return text.encode("latin-1", "ignore").decode("latin-1")


# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF or DOCX)",
    type=["pdf", "docx"]
)

clauses = []
overall = "Unknown"

if uploaded_file is not None:

    # ---- TEXT EXTRACTION ----
    if uploaded_file.type == "application/pdf":
        full_text = extract_text_from_pdf(uploaded_file)
    else:
        full_text = extract_text_from_docx(uploaded_file)

    if not full_text or len(full_text.strip()) < 50:
        st.error("❌ Could not extract readable text from the document.")
        st.stop()

    # ---- CONTRACT CHECK ----
    if not is_likely_contract(full_text):
        st.warning("⚠️ This document may not be a legal contract. Results may be inaccurate.")

    # ---- CLAUSE SPLIT ----
    clauses = split_clauses(full_text)

    if not clauses:
        st.error("❌ No clauses detected.")
        st.stop()

    st.subheader("📌 Clause Analysis")

    # ---- CLAUSE ANALYSIS ----
    for i, clause in enumerate(clauses, start=1):
        risk = score_clause(clause)

        st.markdown(f"### Clause {i}")
        st.markdown(f"**Risk Level:** `{risk}`")
        st.write(clause)
        st.caption(explain_clause_simple(clause))
        st.divider()

    # ---- OVERALL RISK ----
    overall = overall_contract_risk(clauses)
    st.success(f"📊 Overall Contract Risk: **{overall}**")


# -------- PDF EXPORT (SAFE) --------
if clauses and st.button("📄 Export PDF Summary"):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    pdf.cell(0, 10, f"Overall Contract Risk: {overall}", ln=True)
    pdf.ln(5)

    for i, clause in enumerate(clauses, start=1):
        clean_clause = sanitize_text_for_pdf(clause)
        pdf.multi_cell(0, 7, f"Clause {i}:\n{clean_clause}")
        pdf.ln(3)

    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    pdf_buffer = BytesIO(pdf_bytes)

    st.download_button(
        label="⬇️ Download PDF Report",
        data=pdf_buffer,
        file_name="contract_summary.pdf",
        mime="application/pdf"
    )
