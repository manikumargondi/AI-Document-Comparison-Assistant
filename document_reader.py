
"""PDF text extraction and validation using pypdf."""

from io import BytesIO

from pypdf import PdfReader


def extract_pdf_text(uploaded_file):
    """Extract readable text from an uploaded PDF, preserving page numbers."""
    data = uploaded_file.getvalue()

    if not data:
        raise ValueError("The uploaded PDF is empty.")

    try:
        reader = PdfReader(BytesIO(data), strict=True)

        if reader.is_encrypted:
            raise ValueError(
                "This PDF is password-protected. Please upload an "
                "unencrypted PDF."
            )

        if len(reader.pages) == 0:
            raise ValueError("The PDF contains no pages.")

        pages = []

        for page_number, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()

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
            "Unable to read this PDF. Check that it is a valid, "
            "unencrypted PDF."
        ) from exc
