import builtins
import typing


def all_thing_is_obj(obj: typing.Any) -> int:
    """Print the type of some objects and returns 42."""
    t = type(obj)
    match t:
        case builtins.list:
            print("List :", t)
        case builtins.tuple:
            print("Tuple :", t)
        case builtins.set:
            print("Set :", t)
        case builtins.dict:
            print("Dict :", t)
        case builtins.str:
            print(obj, "is in the kitchen :", t)
        case _:
            print("Type not found")
    return 42
