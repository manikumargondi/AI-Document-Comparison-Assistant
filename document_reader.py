
"""PDF text extraction and validation."""

import pymupdf


def extract_pdf_text(uploaded_file):
    """Extract readable text from an uploaded PDF."""
    data = uploaded_file.getvalue()

    if not data:
        raise ValueError("The uploaded PDF is empty.")

    try:
        with pymupdf.open(stream=data, filetype="pdf") as pdf:
            if len(pdf) == 0:
                raise ValueError("The PDF contains no pages.")

            pages = []

            for page_number, page in enumerate(pdf, start=1):
                text = page.get_text().strip()

                if text:
                    pages.append(f"[Page {page_number}]\n{text}")

            extracted_text = "\n\n".join(pages)

            if not extracted_text:
                raise ValueError(
                    "No readable text found. This may be a scanned PDF. "
                    "OCR is not enabled yet."
                )

            return extracted_text

    except ValueError:
        raise
    except Exception as exc:
        raise ValueError(
            "Unable to read this PDF. Check that it is a valid PDF."
        ) from exc
