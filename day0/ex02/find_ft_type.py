import builtins


def all_thing_is_obj(obj: any) -> int:
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
