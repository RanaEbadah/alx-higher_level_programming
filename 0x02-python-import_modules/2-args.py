#!/usr/bin/python3
import sys


def main():
    pluralText = ""
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        if len(sys.argv) > 2:
            pluralText = "s"

        print("{} argument{}:".format(len(sys.argv) - 1, pluralText))

        for arguIndex in range(1, len(sys.argv)):
            print("{}: {}".format(arguIndex, sys.argv[arguIndex]))


if __name__ == "__main__":
    main()
