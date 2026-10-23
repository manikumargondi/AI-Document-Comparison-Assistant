from io import BytesIO

import pymupdf
import pytest

from document_reader import extract_pdf_text


def make_pdf(text="Hello from a test PDF"):
    """Create a small in-memory PDF for testing."""
    document = pymupdf.open()
    page = document.new_page()
    page.insert_text((72, 72), text)
    data = document.tobytes()
    document.close()
    return data


def test_extract_pdf_text_success():
    uploaded_file = BytesIO(make_pdf("Hello test"))
    extracted = extract_pdf_text(uploaded_file)
    assert "Hello test" in extracted
    assert "[Page 1]" in extracted


def test_empty_file_raises_error():
    with pytest.raises(ValueError, match="empty"):
        extract_pdf_text(BytesIO(b""))


def test_invalid_pdf_raises_error():
    with pytest.raises(ValueError, match="Unable to read"):
        extract_pdf_text(BytesIO(b"not a real PDF"))


def test_pdf_without_readable_text_raises_error():
    document = pymupdf.open()
    document.new_page()
    data = document.tobytes()
    document.close()

    with pytest.raises(ValueError, match="No readable text"):
        extract_pdf_text(BytesIO(data))