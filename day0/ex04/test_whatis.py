from whatis import main


def check(capfd, args, expected):
    main(["whatis.py"] + args)
    out, _ = capfd.readouterr()
    assert out == expected


def test_whatis(capfd):
    check(capfd, ["14"], "I'm Even.\n")
    check(capfd, ["-5"], "I'm Odd.\n")
    check(capfd, [], "")
    check(capfd, ["0"], "I'm Even.\n")
    check(capfd, ["Hi!"], "AssertionError: argument is not an integer\n")
    check(capfd, ["13", "5"], "AssertionError: more than one argument is provided\n")
