import sys

sys.tracebacklimit = 0

if len(sys.argv) < 2:
    sys.exit()
assert len(sys.argv) == 2, "more than one argument is provided"
try:
    n: int | None = int(sys.argv[1])
except ValueError:
    n = None
assert n is not None, "argument is not an integer"
print("I'm Odd." if n & 1 else "I'm Even.")
