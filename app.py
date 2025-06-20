#!/usr/bin/env python3
"""
pdf_to_png.py

Usage:
    python pdf_to_png.py input.pdf output_folder [--zoom ZOOM]

Converts each page of input.pdf into a PNG image in output_folder.
"""

import os
import argparse
import fitz  # PyMuPDF

def pdf_to_png(pdf_path: str, output_dir: str, zoom: float = 2.0):
    """
    Convert each page of the PDF at pdf_path into a PNG in output_dir.
    zoom: scale factor (1.0 = original size). Higher → higher resolution.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF
    doc = fitz.open(pdf_path)
    print(f"Opened '{pdf_path}', {doc.page_count} pages to convert.")

    # Matrix for resolution
    mat = fitz.Matrix(zoom, zoom)

    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=mat)
        output_path = os.path.join(output_dir, f"page_{page_index+1:03d}.png")
        pix.save(output_path)
        print(f" Saved page {page_index+1} → {output_path}")

    print("Done.")

def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF pages to PNG images."
    )
    parser.add_argument(
        "pdf", help="Path to the input PDF file."
    )
    parser.add_argument(
        "outdir", help="Folder to save the PNG files."
    )
    parser.add_argument(
        "--zoom", "-z",
        type=float,
        default=2.0,
        help="Resolution zoom factor (default: 2.0)."
    )

    args = parser.parse_args()
    pdf_to_png(args.pdf, args.outdir, args.zoom)

if __name__ == "__main__":
    main()

