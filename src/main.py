#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import re
import colorama
import time
import pyfiglet

from colorama import Fore, Style
from core import args_parser
from core.bar import Loading
from core.search import Search
from core.patterns import patterns

class Application:

    @staticmethod
    def run(args):
        """Main Method"""

        search = Search(patterns[args.pattern], args.output)

        # Draw logo
        print(pyfiglet.figlet_format("Number Founder"))

        print(Fore.LIGHTGREEN_EX + "[Initialisation]" + Style.RESET_ALL)
        Loading.run()

        print(Fore.LIGHTGREEN_EX + "[Prepare Dependencies]" + Style.RESET_ALL)
        Loading.run()

        if args.clipboard:
            print(Fore.LIGHTGREEN_EX + "[Parsing Clipboard]" + Style.RESET_ALL)
            search.in_clipboard()
        elif args.text_file:
            print(Fore.LIGHTGREEN_EX + "[Reading File]" + Style.RESET_ALL)
            search.in_text_file(args.text_file)
        elif args.pdf:
            print(Fore.LIGHTGREEN_EX + "[Reading PDF File]" + Style.RESET_ALL)
            search.in_pdf_file(args.pdf)
        elif args.url:
            print(Fore.LIGHTGREEN_EX + "[Parsing Site By URL]" + Style.RESET_ALL)
            search.on_the_site(args.url)


if __name__ == "__main__":
    try:
        args = args_parser.ArgsParser().create_parser()  # Create CLI's arguments parser
        Application().run(args)
    except KeyboardInterrupt:
        print(Fore.RED + "\nCanceled")
        sys.exit(1)
