# The filename is ft_statistics.py and not statistics.py because the latter
# is a module in the standard library.

import numbers
from typing import Any

FUNCTIONS: Any = {
    "mean": lambda *args: sum(args) / len(args),
    "median": lambda *args: sorted(args)[len(args) // 2],
    "quartile": lambda *args: [
        sorted(args)[len(args) // 4],
        sorted(args)[len(args) * 3 // 4],
    ],
    "var": lambda *args: sum((x - sum(args) / len(args)) ** 2 for x in args)
    / len(args),
    "std": lambda *args: FUNCTIONS["var"](*args) ** 0.5,
}


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print various statistics."""
    for arg in args:
        if not isinstance(arg, numbers.Number):
            print("ERROR")
            return
    for value in kwargs.values():
        if value in FUNCTIONS:
            if args:
                print(value, FUNCTIONS[value](*args), sep=" : ")
            else:
                print("ERROR")
