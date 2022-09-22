import argparse
import sys
import re
import colorama
import time

from colorama import Fore, Back
from core.search import search_in_clipboard, search_in_text_file, \
    search_in_pdf_file, search_on_the_site

colorama.init()

SLEEP_TIME=1.5

def main():

    country_pattern = {
        "RU": r"(\+7)(\s|\W)*(\d{3})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        "BY": r"(\+375)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        "UK": r"(\+380)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
    }

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
    elif args.text_file:
        print(Fore.GREEN + "[Reading File]")
        time.sleep(SLEEP_TIME)
        search_in_text_file(country_pattern[args.pattern], args.text_file, args.output)
    elif args.pdf:
        print(Fore.GREEN + "[Reading PDF file]")
        time.sleep(SLEEP_TIME)
        search_in_pdf_file(country_pattern[args.pattern], args.pdf, args.output)
    elif args.url:
        print(Fore.GREEN + "[Parsing Site By URL]")
        time.sleep(SLEEP_TIME)
        search_on_the_site(country_pattern[args.pattern], args.url, args.output)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="number-founder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=Fore.BLUE + "Found number by pattern in text-files, pdf-files, clipboard or on the sites.",
        usage="%(prog)s -p BY,UK,RU [OPTIONS]",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--clipboard", "-c", action="store_true", help="Searching in clipboard.")
    group.add_argument("--text-file",  "-ft", type=str, help="Searching in text file.", metavar="F")
    group.add_argument("--pdf", type=str, help="Searching in pdf file.", metavar="F")
    group.add_argument("--url", type=str, help="Searching on the site.", metavar="U")

    parser.add_argument("--pattern", "-p", required=True ,type=str, choices=["RU", "BY", "UK"] ,help="Usage define pattern: RU, BY, UK", metavar="P")
    parser.add_argument("--output", "-o", help="Write in file", type=str, metavar="F", default=False)

    args = parser.parse_args()

    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nCanceled")
        sys.exit(0)
