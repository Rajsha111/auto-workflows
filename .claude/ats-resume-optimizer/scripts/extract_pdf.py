#!/usr/bin/env python3
"""
Extract text from a PDF resume.
Tries pdfplumber first (better layout preservation), falls back to PyPDF2.

Usage:
    python extract_pdf.py <path-to-resume.pdf>

Output:
    Prints extracted text to stdout.
"""

import sys
import os


def extract_with_pdfplumber(pdf_path):
    import pdfplumber
    text_parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return "\n\n".join(text_parts)


def extract_with_pypdf2(pdf_path):
    import PyPDF2
    text_parts = []
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return "\n\n".join(text_parts)


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <path-to-resume.pdf>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"Error: file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Try pdfplumber first
    try:
        text = extract_with_pdfplumber(pdf_path)
        print(text)
        return
    except ImportError:
        pass
    except Exception as e:
        print(f"pdfplumber failed ({e}), trying PyPDF2...", file=sys.stderr)

    # Fallback to PyPDF2
    try:
        text = extract_with_pypdf2(pdf_path)
        print(text)
        return
    except ImportError:
        print("Neither pdfplumber nor PyPDF2 is installed.", file=sys.stderr)
        print("Install with: pip install pdfplumber", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"PyPDF2 also failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
