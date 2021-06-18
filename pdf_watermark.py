"""
    Watermark each page of pdf files.
    Pass as command arguments the pdf filenames you want watermarked and last the pdf filename with the watermark.
"""

import PyPDF2
from sys import argv

pdf_files = argv[1:-1]
watermark = argv[-1]

def watermark_pdfs(pdf_files, watermark):
    for pdf_file in pdf_files:

        with open(pdf_file, "rb") as pdf_file:
            # Reading content of the pdf file.
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            # Reading the content of the watermark file
            with open(watermark, "rb") as watermark_file:
                watermark_reader = PyPDF2.PdfFileReader(watermark_file)

                page_number = 0

                watermark_page = watermark_reader.getPage(page_number)
                    
                pdf_writer = PyPDF2.PdfFileWriter()

                while page_number < pdf_reader.getNumPages():
                    pdf_page = pdf_reader.getPage(page_number)

                    pdf_page.mergePage(watermark_page)

                    pdf_writer.addPage(pdf_page)

                    with open(f"watermarked_{pdf_file.name}", mode="wb") as watermarked_pdf_file:
                        pdf_writer.write(watermarked_pdf_file)
                    page_number += 1


watermark_pdfs(pdf_files, watermark)
