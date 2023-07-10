from string import punctuation
import sys


def count_pred(s, pred):
    return sum(map(pred, s))


def main(s):
    if not s:
        print("What is the text to count?")
        s = sys.stdin.readline()
    print(f"The text contains {len(s)} characters:")
    print(f"{count_pred(s, str.isupper)} upper letters")
    print(f"{count_pred(s, str.islower)} lower letters")
    print(f"{count_pred(s, punctuation.__contains__)} punctuation marks")
    print(f"{count_pred(s, str.isspace)} spaces")
    print(f"{count_pred(s, str.isdigit)} digits")


if __name__ == "__main__":
    assert len(sys.argv) <= 2, "Too many arguments"
    main(sys.argv[1] if len(sys.argv) == 2 else None)
