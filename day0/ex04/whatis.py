import re
import sys

sys.excepthook = lambda type, value, _: print(
    f"{type.__name__}: {value}", file=sys.stderr
)

if len(sys.argv) < 2:
    sys.exit()
assert len(sys.argv) == 2, "more than one argument is provided"
assert re.fullmatch(r"-?\d+", sys.argv[1]), "argument is not an integer"
print("I'm Odd." if ord(sys.argv[1][-1]) & 1 else "I'm Even.")
