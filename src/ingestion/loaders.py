import pymupdf

def validate_format(filename: str) -> bool:
    """Check if the file has a .pdf extension."""
    return filename.lower().endswith(".pdf")


def check_empty(content: bytes) -> bool:
    """Check if the uploaded file content is empty (0 bytes)."""
    return len(content) == 0


def read_pdf(content: bytes):
    """
    Attempt to open and read the PDF using pymupdf.
    Returns the document object on success, or None on failure.
    """
    try:
        doc = pymupdf.open(stream=content, filetype="pdf")
        return doc
    except Exception:
        return None