
import pytesseract
import os
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
from PyPDF2 import PdfFileMerger, PdfFileReader
from io import FileIO as file
import json

def searchable_pdf(pdf_file):
    input_file_name = os.path.basename(pdf_file).split(".")[0]
    output_file_name = input_file_name + "_converted.pdf"
    images = convert_from_path(pdf_file)
    pdf_pages = [pytesseract.image_to_pdf_or_hocr(image, extension='pdf') for image in images]
    with open(output_file_name, "wb") as f:
        f.write(pdf_pages[0])
    if len(pdf_pages)>1:
        for i in range(len(pdf_pages)-1):
            with open("append.pdf", "wb") as f:
                f.write(pdf_pages[i+1])
            merger = PdfFileMerger()
            merger.append(PdfFileReader(file(output_file_name, 'rb')))
            merger.append(PdfFileReader(file("append.pdf", 'rb')))
            merger.write(output_file_name)
    os.remove("append.pdf")
    print("searchable pdf created")


def extract_text(pdf_file):
    input_file_name = os.path.basename(pdf_file).split(".")[0]
    output_file_name = input_file_name + ".json"
    images = convert_from_path(pdf_file)
    txt_pages = [pytesseract.image_to_string(image) for image in images]
    with open(output_file_name, 'w') as f:
        json.dump(txt_pages, f)
    print("text extracted into json file")
