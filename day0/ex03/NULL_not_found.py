import math
import typing


def NULL_not_found(obj: typing.Any) -> int:
    """Print the type of falsy objects."""
    if type(obj) is float and math.isnan(obj) or not obj:
        print(obj, type(obj))
        return 0
    else:
        print("Type not Found")
        return 1
