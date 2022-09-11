import argparse
import sys
import re

from core.search import look_for_in_clipboard, look_for_in_text_file

def main():

    if not args.pattern:
        print("Pattern not founded!")
        sys.exit(1)

    if args.clipboard:
        look_for_in_clipboard(args.pattern)
        
    elif args.file-txt:
        look_for_in_text_file(pattern, args.file-txt)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="number-founder",
        description="Found number by pattern in file or clipboar",
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--clipboard", "-c", action="store_true", help="Looking for number in clipboard.")
    group.add_argument("--file-txt", "-ft", type=str, help="Looking for number in text file.", metavar="FILE")

    parser.add_argument("--pattern", "-p", type=str, help="Usage own pattern.", metavar="PATTERN")
    parser.add_argument("--output", "-o", help="Write in file", type=str, metavar="FILE")

    args = parser.parse_args()

    try:
        main()
    except KeyboardInterrupt:
        print("\nCanceled")
        sys.exit(0)