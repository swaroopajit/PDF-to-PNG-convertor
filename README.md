# PDF to PNG Converter

A simple Python script that converts each page of a PDF file into separate PNG image files, using PyMuPDF (also known as `fitz`).

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)

  * [Command-Line Arguments](#command-line-arguments)
  * [Examples](#examples)
* [Alternative Backend](#alternative-backend)
* [License](#license)

## Features

* Converts each page of a PDF into its own PNG file.
* Adjustable resolution via a zoom factor.
* Creates the output directory if it doesn't exist.
* Prints progress to the console.

## Prerequisites

* Python 3.6 or newer
* Pip package manager

## Installation

1. Clone or download this repository.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```bash
python pdf_to_png.py <input.pdf> <output_folder> [--zoom ZOOM]
```

### Command-Line Arguments

* `<input.pdf>`: Path to the source PDF file.
* `<output_folder>`: Directory where PNG files will be saved.
* `--zoom ZOOM` or `-z ZOOM` (optional): Scale factor for resolution.

  * Default: `2.0` (twice the PDF’s native resolution).
  * Higher values produce higher-resolution PNGs.

### Examples

* **Basic conversion** with default zoom:

  ```bash
  python pdf_to_png.py document.pdf images
  ```

  This creates `images/page_001.png`, `images/page_002.png`, etc., at 2× resolution.

* **Custom resolution** (e.g., 3×):

  ```bash
  python pdf_to_png.py document.pdf highres_images --zoom 3.0
  ```

## License

This project is released under the MIT License. Feel free to use and modify as needed.

