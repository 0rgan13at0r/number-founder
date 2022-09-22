import re
import pyperclip
import sys
import PyPDF2
import colorama
import requests

from colorama import Fore, Back
from pathlib import Path
from time import sleep

colorama.init()

def search_in_clipboard(pattern: str, output_file: str):
    data = pyperclip.paste()
    _find_number(pattern, data, output_file)


def search_in_text_file(pattern: str, file_to: str, output_file: str):
    data = ""

    if not Path(file_to).exists():
        print(Fore.RED + "File wasn't founded!!")
        sys.exit(1)

    with open(file_to, "r") as file:
        data += file.read()

    _find_number(pattern, data, output_file)


def search_in_pdf_file(pattern: str, file_to: str, output_file: str):
    data = ""

    with open(file_to, "rb") as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        count_pages = pdfReader.numPages

        for page in range(count_pages):
            pageObj = pdfReader.getPage(page)
            data += pageObj.extractText()

    _find_number(pattern, data, output_file)


def search_on_the_site(pattern: str, url: str, output_file: str):
    data = ""

    try:
        response = requests.get(url)
        data += response.text
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Connection Failed!")
        sys.exit(1)

    _find_number(pattern, data, output_file)


def _find_number(pattern: str, data, output_file: str):
    numbers_count = 0

    for number in re.findall(pattern, data):
            sleep(0.05)

            print(Fore.WHITE + f"Found: {''.join(number)}")
            numbers_count += 1

            if output_file:
                _output(output_file, f"{''.join(number)}\n")

    if numbers_count != 0:
        print(Fore.BLUE + f"\nNumbers count: {numbers_count}")
    else:
        print(Fore.RED + "No numbers!")


def _output(file_to: str, data: str):
    with open(file_to, "a") as file:
        file.write(data)
