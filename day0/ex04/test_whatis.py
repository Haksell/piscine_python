import os
import subprocess


def check(args, stdout, stderr):
    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "whatis.py"
    )
    result = subprocess.run(
        ["python", script_path] + args, text=True, capture_output=True
    )
    assert result.stdout == stdout
    assert result.stderr == stderr


def test_whatis():
    check(["14"], "I'm Even.\n", "")
    check(["-5"], "I'm Odd.\n", "")
    check([], "", "")
    check(["0"], "I'm Even.\n", "")
    check(["Hi!"], "", "AssertionError: argument is not an integer\n")
    check(
        ["13", "5"],
        "",
        "AssertionError: more than one argument is provided\n",
    )
