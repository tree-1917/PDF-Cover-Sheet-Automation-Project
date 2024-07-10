# PDF Cover Sheet Automation Project

This project automates the task of adding a cover sheet to all PDF files in the input directory and saving the modified PDFs with a cover sheet to the output directory. 📄🤖

## Project Overview

The goal of this project is to streamline the process of adding a cover sheet to multiple PDF files. This automation script performs the following tasks:

1. **Get all PDF files in the current directory**: It identifies all PDF files in the specified `input` directory. 📂

2. **Open and read PDF files**: It opens each PDF file, reads its pages, and prepares to add a cover sheet. 📖

3. **Add cover sheet**: It adds a cover sheet (specified as `cover_sheet.pdf` in the `input` directory) to each PDF file and saves the modified PDF with a new name in the `output` directory. 🖼️

## Instructions

### Setup

1. Place all PDF files that need a cover sheet in the `input` directory. 📁
2. Ensure there is a `cover_sheet.pdf` file in the `input` directory, which will be used as the cover sheet template. 📄

### Running the Script

1. Run the script `add_cover_sheet.py` to execute the automation. 🚀
2. After execution, check the `output` directory for the modified PDF files with the cover sheet added. 📂

### Notes

- Make sure to customize the script or adjust paths if your directory structure or file names differ. 🛠️
- This script uses PyPDF2 library for PDF manipulation. Ensure it's installed (`pip install PyPDF2`) before running the script. 📦

Feel free to modify and extend this script according to your specific needs! 🎨

---

