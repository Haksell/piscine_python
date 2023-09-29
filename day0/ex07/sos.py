import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def main(argv):
    """Print the morse code of the given string."""
    assert len(argv) == 2, "the arguments are bad"
    s = argv[1].upper()
    assert type(s) is str and all(c in NESTED_MORSE for c in s)
    print(" ".join(NESTED_MORSE[c] for c in s))


if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main(sys.argv)
    except AssertionError as e:
        print(f"{e.__class__.__name__}: the arguments are bad", file=sys.stderr)
