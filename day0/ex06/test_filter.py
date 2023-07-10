from filterstring import main
from ft_filter import ft_filter
from itertools import tee
import math


def test_doc():
    assert filter.__doc__ == ft_filter.__doc__


def check_function(func, seq):
    seq, cpy = tee(seq)
    assert list(ft_filter(func, seq)) == list(filter(func, cpy))


def test_none():
    check_function(
        None, [None, 0, 0.0, "", [], {}, 1, "Hello World", math.nan]
    )


def test_filter():
    check_function(lambda x: x % 2 == 0, range(10))
    check_function(str.isupper, "Hello World")
    check_function(lambda s: len(s) > 3, ["Hello", "World", "!"])


def check_program(capfd, args, expected):
    main(["filterstring.py"] + args)
    out, _ = capfd.readouterr()
    assert out == expected


def test_program(capfd):
    check_program(capfd, ["Hello the World", 4], "['Hello', 'World']\n")
    check_program(capfd, ["Hello the World", 99], "[]\n")
    check_program(
        capfd,
        [3, "Hello the World"],
        "AssertionError: the arguments are bad\n",
    )
    check_program(capfd, [], "AssertionError: the arguments are bad\n")
