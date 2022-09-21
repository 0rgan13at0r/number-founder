import re
import pyperclip
import sys
import PyPDF2

from pathlib import Path
from time import sleep


def search_in_clipboard(pattern: str, output_file: str):
    not_filter_data = pyperclip.paste()
    _find_number(pattern, not_filter_data, output_file)


def search_in_text_file(pattern: str, file_to: str, output_file: str):

    if not Path(file_to).exists():
        print("File wasn't founded!!")
        sys.exit(1)

    with open(file_to, "r") as file:
        not_filter_data = file.read()
        _find_number(pattern, not_filter_data, output_file)


def search_in_pdf_file(pattern: str, file_to: str, output_file: str):
    data = ""

    with open(file_to, "rb") as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        count_pages = pdfReader.numPages

        for page in range(count_pages):
            pageObj = pdfReader.getPage(page)
            data += pageObj.extractText()

    _find_number(pattern, data, output_file)
    

def _find_number(pattern: str, data, output_file: str):
    numbers_count = 0

    for number in re.findall(pattern, data):
            sleep(0.05)

            print(f"Found: {''.join(number)}")
            numbers_count += 1

            if output_file:
                _output(output_file, f"{''.join(number)}\n")

    print(f"Done\nNumbers count: {numbers_count}")


def _output(file_to: str, data: str):
    with open(file_to, "a") as file:
        file.write(data)
