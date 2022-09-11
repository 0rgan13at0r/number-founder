import re
import pyperclip
import sys

from pathlib import Path
from time import sleep


def look_for_in_clipboard(pattern: str, output_file: str):
    numbers_count = 0

    for number in re.findall(pattern, pyperclip.paste()):
        sleep(0.03)

        print(f"Found: +{''.join(number)}")
        numbers_count += 1

        if output_file:
            _output(output_file, f"+{''.join(number)}")

    print(f"Done\nNumbers count: {numbers_count}")


def look_for_in_text_file(pattern: str, file_to: str, output_file: str):
    numbers_count = 0

    if not Path(file_to).exists():
        print("File wasn't founded!!")
        sys.exit(1)

    with open(file_to, "r") as file:
        for number in re.findall(pattern, file.read()):
            sleep(0.03)

            print(f"Found: +{''.join(number)}")
            numbers_count += 1

            if output_file:
                _output(output_file, f"+{''.join(number)}")

        print(f"Done\nNumbers count: {numbers_count}")


def _output(file_to: str, data: str):
    with open(file_to, "w") as file:
        file.write(data) 


# if __name__ == "__main__":
#     reg = re.compile(r"\+(\d{3})(\s|\S)?(\d{2})(\s|\S)?(\d{3})(\s|\S)?(\d{2})(\s|\S)?(\d{2})")
#     look_for_in_clipboard(reg)
#     look_for_in_text_file(reg, "src/core/temp.txt")