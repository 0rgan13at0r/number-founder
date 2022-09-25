import re
import pyperclip
import sys
import PyPDF2
import colorama
import requests
import time
import random

from colorama import Fore, Back
from pathlib import Path
from .output import Output
from .useragents import useragents

class Search:

    def __init__(self, pattern, output_file):
        self.pattern = pattern
        self.output_file = output_file
        self.numbers_count = 0

        colorama.init()

    def in_clipboard(self):
        """Search numbers in the clipboard."""
        data = pyperclip.paste()
        self._find_number(data)

    def in_text_file(self, file_to):
        """Search numbers in the text file."""
        if not Path(file_to).exists():
            print(Fore.RED + "File wasn't founded!")
            sys.exit(1)

        data = self._read_file(file_to)
        self._find_number(data)

    def in_pdf_file(self, file_to):
        """Search numbers in the pdf file."""
        data = ""

        with open(file_to, "rb") as file:
            pdfReader = PyPDF2.PdfFileReader(file)
            count_pages = pdfReader.numPages

            for page in range(count_pages):
                pageObj = pdfReader.getPage(page)
                data += pageObj.extractText()

        self._find_number(data)

    def on_the_site(self, url):
        """Search numbers on the site."""
        try:
            data = self._get_data_for_site(url)
            self._find_number(data)
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "Connection Failed!")
            sys.exit(1)

    def _get_data_for_site(self, url):
        headers = {
            'User-Agent': random.choice(useragents), # Initialisate random User-Agent.
            'Accept': '*/*',
        }

        response = requests.get(url, headers=headers)
        return response.text

    def _read_file(self, file_to):
        """Get text in the texting file."""
        with open(file_to, "r") as file:
            return file.read()

    def _find_number(self, data):
        """Main method. Parsing numbers on the data that is getting."""
        for number in re.findall(self.pattern, data):
            time.sleep(0.05)

            # Formatting numbers. Delete all doesn't need elements.
            formated_number = re.sub(r"\D", "", "".join(number))

            print(Fore.WHITE + f"Found: +{''.join(formated_number)}")
            self.numbers_count += 1

            # Write data in a file.
            if self.output_file:
                Output.write_to_file(self.output_file, f"+{''.join(formated_number)}\n")

        if self.numbers_count == 0:
            print(Fore.RED + "No numbers!")
        else:
            print(Fore.LIGHTYELLOW_EX + f"\nNumbers count: {self.numbers_count}")
