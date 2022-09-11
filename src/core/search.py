import re
import pyperclip

from time import sleep


def look_for_in_clipboard(pattern: str):
    numbers_count = 0

    for number in re.findall(pattern, pyperclip.paste()):
        sleep(0.03)

        print(f"Found: +{''.join(number)}\n")
        numbers_count += 1

    print(f"Done\nNumbers count: {numbers_count}")


# if __name__ == "__main__":
#     reg = re.compile(r"\+(\d{3})(\s|\S)?(\d{2})(\s|\S)?(\d{3})(\s|\S)?(\d{2})(\s|\S)?(\d{2})")
#     look_for_in_clipboard(reg)