import re
from ft_filter import ft_filter
import sys
import traceback


def main(argv):
    """Print the words of a string that are longer than n."""
    try:
        assert len(argv) == 3 and re.fullmatch(
            r"-?\d+", argv[2]
        ), "the arguments are bad"
    except AssertionError:
        traceback.print_exc(0)
        return
    words = argv[1].split(" ")
    n = int(argv[2])
    print([w for w in ft_filter(lambda w: len(w) > n, words)])


if __name__ == "__main__":
    main(sys.argv)
