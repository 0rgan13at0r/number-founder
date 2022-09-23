import re
import pyperclip
import sys
import PyPDF2
import colorama
import requests

from fake_useragent import UserAgent
from colorama import Fore, Back
from pathlib import Path
from time import sleep
from .output import output

colorama.init()

def search_in_clipboard(pattern, output_file):
    data = pyperclip.paste()
    _find_number(pattern, data, output_file)

def search_in_text_file(pattern, file_to, output_file):
    data = ""

    if not Path(file_to).exists():
        print(Fore.RED + "File wasn't founded!")
        sys.exit(1)

    with open(file_to, "r") as file:
        data += file.read()

    _find_number(pattern, data, output_file)

def search_in_pdf_file(pattern, file_to, output_file):
    data = ""

    with open(file_to, "rb") as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        count_pages = pdfReader.numPages

        for page in range(count_pages):
            pageObj = pdfReader.getPage(page)
            data += pageObj.extractText()

    _find_number(pattern, data, output_file)

def search_on_the_site(pattern, url, output_file):
    data = ""

    try:
        data = _get_data_for_site(url)
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Connection Failed!")
        sys.exit(1)

    _find_number(pattern, data, output_file)

def _get_data_for_site(url):
    fake_agent = UserAgent()

    headers = {
        'User-Agent': fake_agent.google, # Initialisate random User-Agent.
        'Accept': '*/*',
    }

    response = requests.get(url, headers=headers)
    return response.text

def _find_number(pattern, data, output_file):
    numbers_count = 0

    for number in re.findall(pattern, data):
            sleep(0.05)

            # Formatting numbers. Delete all doesn't need elements.
            formated_number = re.sub(r"\D", "", "".join(number))

            print(Fore.WHITE + f"Found: +{''.join(formated_number)}")
            numbers_count += 1

            # Write data in a file.
            if output_file:
                output(output_file, f"+{''.join(formated_number)}\n")

    _get_info(numbers_count, output_file)

def _get_info(numbers_count, output_file):
    if numbers_count != 0:
        print(Fore.LIGHTYELLOW_EX + f"\nNumbers count: {numbers_count}")
    else:
        print(Fore.RED + "No numbers!")

    if output_file:
        print(Fore.LIGHTYELLOW_EX + f"File {output_file} succesfull saved.")
