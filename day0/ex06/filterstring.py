from ft_filter import ft_filter
import sys


def main(argv):
    """Print the words of a string that are longer than n."""
    # print(argv)
    assert len(argv) == 3
    try:
        n = int(argv[2])
    except ValueError:
        n = None
    assert n is not None
    words = argv[1].split(" ")
    print([w for w in ft_filter(lambda w: len(w) > n, words)])


if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main(sys.argv)
    except AssertionError as e:
        print(f"{e.__class__.__name__}: the arguments are bad", file=sys.stderr)
