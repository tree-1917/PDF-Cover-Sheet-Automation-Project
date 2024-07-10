# --- Adding Cover Sheet to PDF files --- #
from PyPDF2 import PdfReader, PdfWriter
import os

# TODO 1 - Get all PDF files in the current directory

list = os.listdir("./input")
output = './output'
if not os.path.exists(output):
    os.mkdir(output)
    print('output directory created .')
# Cover sheet
cover_reader = PdfReader('./input/cover_sheet.pdf')

# TODO 2 - Open all pdf files and read pages
for file in list:
    if file == 'cover_sheet.pdf':
        continue
    pdf_writer = PdfWriter()
    pdf_writer.add_page(cover_reader.pages[0])  # create cover writer
    pdf_reader = PdfReader(f'./input/{file}')
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)
    # TODO 3 - Add cover sheet to the files and save to new directory with new name
    with open(f'./output/covered{file}', 'wb') as f:
        pdf_writer.write(f)
