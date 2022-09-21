import argparse
import sys
import re

from core.search import search_in_clipboard, search_in_text_file, search_in_pdf_file

def main():

    country_pattern = {
        "RU": r"(\+7)(\s|\W)*(\d{3})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        "BY": r"(\+375)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        "UK": r"(\+380)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
    }

    if not args.pattern in "RU BY UK".split():
        print("Pattern not founded!")
        sys.exit(1)

    if args.clipboard:
        search_in_clipboard(country_pattern[args.pattern], args.output)
    elif args.file:
        search_in_text_file(country_pattern[args.pattern], args.file_txt, args.output)
    elif args.pdf:
        search_in_pdf_file(country_pattern[args.pattern], args.pdf, args.output)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="number-founder",
        description="Found number by pattern in file or clipboard",
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
        print("\nCanceled")
        sys.exit(0)
