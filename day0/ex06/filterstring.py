from ft_filter import ft_filter
import sys


def main(argv):
    """Print the words of a string that are longer than n."""
    try:
        assert len(argv) == 3
        s = argv[1]
        n = int(argv[2])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return
    words = s.split(" ")
    print(list(ft_filter(lambda w: len(w) > n, words)))


if __name__ == "__main__":
    main(sys.argv)
