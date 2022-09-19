import re
import pyperclip
import sys

from pathlib import Path
from time import sleep


def look_for_in_clipboard(pattern: str, output_file: str):
    not_filter_data = pyperclip.paste()

    _find_number(pattern, not_filter_data, output_file)


def look_for_in_text_file(pattern: str, file_to: str, output_file: str):

    if not Path(file_to).exists():
        print("File wasn't founded!!")
        sys.exit(1)

    with open(file_to, "r") as file:
        not_filter_data = file.read()

        _find_number(pattern, not_filter_data, output_file)


def _find_number(pattern: str, func, output_file: str):
    numbers_count = 0

    for number in re.findall(pattern, func):
            sleep(0.05)

            print(f"Found: {''.join(number)}")
            numbers_count += 1

            if output_file:
                _output(output_file, f"+{''.join(number)}")

    print(f"Done\nNumbers count: {numbers_count}")


def _output(file_to: str, data: str):
    with open(file_to, "w") as file:
        file.write(data)
