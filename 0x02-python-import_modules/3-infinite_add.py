#!/usr/bin/python3
import sys
argv = sys.argv


def main():
    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print("{}".format(argv[1]))
    else:
        result = 0
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))


if __name__ == "__main__":
    main()
