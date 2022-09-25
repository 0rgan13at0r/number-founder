#!/usr/bin/python3
# -- coding: UTF-8 --

import sys
import re
import colorama
import time

from colorama import Fore, Back
from core import args_parser
from core.bar import Loading
from core.search import Search

class Application:

    def __init__(self):
        self.patterns = {
            "RU": r"(\+7)(\s|\W)*(\d{3})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
            "BY": r"(\+375)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
            "UA": r"(\+380)(\s|\W)*(\d{2})(\s|\W)*(\d{3})(\s|\W)*(\d{2})(\s|\W)*(\d{2})",
        }

    def run(self, args):
        """Main Method"""

        search = Search(self.patterns[args.pattern], args.output)

        print("[Initialisation]")
        Loading.run()

        print("[Prepare Dependencies]")
        Loading.run()

        if args.clipboard:
            self._show_color_text("[Parsing Clipboard]")
            search.in_clipboard()
        elif args.text_file:
            self._show_color_text("[Reading File]")
            search.in_text_file(args.text_file)
        elif args.pdf:
            self._show_color_text("[Reading PDF File]")
            search.in_pdf_file(args.pdf)
        elif args.url:
            self._show_color_text("[Parsing Site By URL]")
            search.on_the_site(args.url)

    def _show_color_text(self, text, SLEEP_TIME=0.05):
        colorama.init()
        print(Fore.LIGHTGREEN_EX + f"{text}")
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    try:
        # Create CLI's arguments parser
        args = args_parser.ArgsParser().create_parser()

        # Start application
        Application().run(args)
    except KeyboardInterrupt:
        print(Fore.RED + "\nCanceled")
        sys.exit(1)
