import argparse

class ArgsParser:

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser(
                prog="number-founder",
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description="Found number by pattern in text-files, pdf-files, clipboard or on the sites.",
                usage="%(prog)s -p BY,UA,RU [OPTIONS]",
            )

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--clipboard", "-c", action="store_true", help="Searching in clipboard.")
        group.add_argument("--text-file",  "-ft", type=str, help="Searching in text file.", metavar="F")
        group.add_argument("--pdf", type=str, help="Searching in pdf file.", metavar="F")
        group.add_argument("--url", type=str, help="Searching on the site.", metavar="U")

        parser.add_argument("--pattern", "-p", required=True ,type=str, choices=["RU", "BY", "UA"] ,help="Usage define pattern: (RU,BY,UA)", metavar="P")
        parser.add_argument("--output", "-o", help="Write in file", type=str, metavar="F", default=False)

        return parser.parse_args()
