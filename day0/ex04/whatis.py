import sys


def main(argv):
    argc = len(argv)
    print(argv, file=sys.stderr)
    match argc:
        case 2:
            try:
                n = int(argv[1])
                print("I'm Odd." if n & 1 else "I'm Even.")
            except ValueError:
                print("AssertionError: argument is not an integer")
        case _ if argc >= 3:
            print("AssertionError: more than one argument is provided")


if __name__ == "__main__":
    main(sys.argv)
