# GenAI Legal Assistant (Hackathon Project)

🎥 Demo Video:
https://drive.google.com/file/d/1CEdetuW3eX_kwQxUvBmgx8H3BfcMbA4O/view?usp=drive_link
GENAI-POWERED LEGAL ASSISTANT FOR SMEs
Project Title:
GenAI-Powered Legal Assistant for Small and Medium Enterprises (SMEs)
Project Description:
This project is a Streamlit-based AI Legal Assistant designed to help Small and Medium Enterprises (SMEs) understand legal contracts more easily. Legal documents are often lengthy and complex, making them difficult for non-legal professionals to interpret. This tool simplifies contract analysis by extracting clauses, explaining them in plain language, identifying potential risks, and generating a downloadable summary report.
The system works completely offline, does not rely on external legal databases, and is intended for educational and assistive purposes only.
Disclaimer:
This application does NOT replace a licensed legal professional.
It is meant for academic, demo, and preliminary analysis use only.
Core Features:
Contract upload (PDF or DOCX)
Automatic text extraction
Clause and sub-clause separation
Clause-by-clause analysis
Plain-language explanation for each clause
Clause-level risk classification (Low / Medium / High)
Overall contract risk assessment
PDF summary export
Multilingual support (English and Hindi input)

Supported File Formats:
PDF (text-based)
DOCX
Plain text (extensible)
Legal NLP Capabilities:
Contract type detection (rule-based)
Clause extraction
Identification of:
Termination clauses
Payment and fee clauses
Confidentiality clauses
Jurisdiction and governing law clauses
Risk assessment using heuristic logic
Detection of non-contract documents (warnings shown)
Multilingual Handling:
Supports English and Hindi documents
Hindi text is internally normalized to English
Output explanations are provided in simple business English
Technology Stack:
Frontend / UI:
Streamlit
Backend / NLP:
Python
spaCy
PyPDF2

python-docx

AI & Reasoning:
Rule-based legal NLP
Deterministic clause logic
No external legal APIs or case law used
PDF Export:

Generates a downloadable PDF summary

Includes overall contract risk and clause details

Project Structure:

genai-legal-assistant/
|
|-- app.py (Main Streamlit application)
|-- nlp_utils.py (Text extraction & clause splitting)
|-- risk_scoring.py (Risk scoring logic)
|-- requirements.txt (Python dependencies)
|-- README.txt (Project documentation)

How to Run Locally:

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

Deployment:

The application can be deployed using Streamlit Community Cloud.

Deployment Requirements:

Code hosted on GitHub

Public repository

requirements.txt included

Privacy & Data Handling:

No contract data is stored permanently

No third-party legal data sources used

All processing is done in-memory

Suitable for confidential documents in demo scenarios

Limitations:

Not a substitute for professional legal advice

Works best with structured legal contracts

Scanned PDFs without OCR are not supported

Risk detection is rule-based, not case-law trained

Future Enhancements:

Named Entity Recognition (Parties, Dates, Amounts)

Obligation vs Right vs Prohibition detection

Clause similarity matching with standard templates

SME-friendly contract template generator

JSON-based audit logs

Enhanced multilingual output

Author:
Nallabothu Jaswanth
B.Tech Computer Science and Engineering(AIML)

