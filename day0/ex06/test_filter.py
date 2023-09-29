import os
from ft_filter import ft_filter
from itertools import tee
import math
import subprocess


def test_doc():
    assert filter.__doc__ == ft_filter.__doc__


def check_function(func, seq):
    seq, cpy = tee(seq)
    assert list(ft_filter(func, seq)) == list(filter(func, cpy))


def test_none():
    check_function(None, [None, 0, 0.0, "", [], {}, 1, "Hello World", math.nan])


def test_filter():
    check_function(lambda x: x % 2 == 0, range(10))
    check_function(str.isupper, "Hello World")
    check_function(lambda s: len(s) > 3, ["Hello", "World", "!"])


def check_program(args, expected_stdout, expected_stderr):
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "filterstring.py"
    )
    result = subprocess.run(
        ["python", script_path] + list(map(str, args)), text=True, capture_output=True
    )
    assert result.stdout == expected_stdout
    assert result.stderr == expected_stderr


def test_program():
    check_program(["Hello the World", 4], "['Hello', 'World']\n", "")
    check_program(["Hello the World", 99], "[]\n", "")
    check_program(
        [3, "Hello the World"],
        "",
        "AssertionError: the arguments are bad\n",
    )
    check_program(["Hello the World"], "", "AssertionError: the arguments are bad\n")
    check_program(
        ["Hello the World", 3, 4], "", "AssertionError: the arguments are bad\n"
    )
