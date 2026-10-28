\# AI Document Comparison Assistant



An AI-powered web application that compares two PDF documents using Google's Gemini API and generates a structured comparison report.



\## Features



\- Upload two PDF documents.

\- Extract readable text from PDFs.

\- Compare summaries, similarities, differences, and key details.

\- Generate a conclusion and identify limitations.

\- Download comparison reports in PDF and DOCX formats.

\- Validate AI-generated comparison results.



\## Technology Stack



\- Python

\- Streamlit

\- Google Gemini API

\- pypdf

\- python-docx

\- ReportLab

\- pytest



\## Requirements



\- Python 3.10 or newer

\- A Google Gemini API key

\- Internet access for AI-powered comparisons



\## Run Locally



1\. Clone or download this repository.

2\. Open Command Prompt in the project directory.

3\. Create a virtual environment:



&#x20;  ```cmd

&#x20;  python -m venv .venv

&#x20;  ```



4\. Activate it:



&#x20;  ```cmd

&#x20;  .venv\\Scripts\\activate

&#x20;  ```



5\. Install dependencies:



&#x20;  ```cmd

&#x20;  python -m pip install -r requirements.txt

&#x20;  ```



6\. Create a `.env` file based on `.env.example` and add your own Gemini API key.

7\. Start the application:



&#x20;  ```cmd

&#x20;  streamlit run app.py

&#x20;  ```



8\. Open the local URL displayed in the terminal.



\## Run Tests



```cmd

python -m pytest -q

```



\## Security



Keep your Gemini API key private. Never commit `.env` or Streamlit secrets to GitHub.



\## Limitations



Comparison quality depends on the text extracted from the uploaded PDFs and the availability of the Gemini API. Scanned PDFs may require OCR if they contain no extractable text. Review generated reports before relying on them for important decisions.
