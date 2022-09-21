import argparse
import sys
import re
import colorama
import time

from colorama import Fore, Back
from core.search import search_in_clipboard, search_in_text_file, search_in_pdf_file

colorama.init()

SLEEP_TIME=1.5

def main():

    country_pattern = {
        "RU": r"(\+7)(\s|\W)*(\d{3})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        "BY": r"(\+375)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        "UK": r"(\+380)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
    }

    if not args.pattern in "RU BY UK".split():
        print(Fore.RED + "Pattern not founded!")
        sys.exit(1)

    time.sleep(SLEEP_TIME)
    print(Fore.GREEN + "[Initialisation]")
    time.sleep(SLEEP_TIME)
    print(Fore.BLUE + "Done\n")
    time.sleep(SLEEP_TIME)
    print(Fore.GREEN + "[Prepare Dependencies]")
    time.sleep(SLEEP_TIME)
    print(Fore.BLUE + "Done\n")
    time.sleep(SLEEP_TIME)

    if args.clipboard:
        print(Fore.GREEN + "[Parsing Clipboard]")
        time.sleep(SLEEP_TIME)
        search_in_clipboard(country_pattern[args.pattern], args.output)
    elif args.file:
        print(Fore.GREEN + "[Reading File]")
        time.sleep(SLEEP_TIME)
        search_in_text_file(country_pattern[args.pattern], args.file_txt, args.output)
    elif args.pdf:
        print(Fore.GREEN + "[Reading PDF file]")
        time.sleep(SLEEP_TIME)
        search_in_pdf_file(country_pattern[args.pattern], args.pdf, args.output)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="number-founder",
        description=Fore.BLUE + "Found number by pattern in text-files, pdf-files and clipboard.",
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--clipboard", "-c", action="store_true", help="Searching in clipboard.")
    group.add_argument("--file",  "-ft", type=str, help="Searching in text file.", metavar="F")
    group.add_argument("--pdf", type=str, help="Searchin in pdf file.", metavar="F")

    parser.add_argument("--pattern", "-p", type=str, help="Usage define pattern: RU, BY, UK", metavar="P")
    parser.add_argument("--output", "-o", help="Write in file", type=str, metavar="F", default=False)

    args = parser.parse_args()

    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nCanceled")
        sys.exit(0)
