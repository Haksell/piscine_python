import math


def NULL_not_found(obj: any) -> int:
    if type(obj) == float and math.isnan(obj) or not obj:
        print(obj, type(obj))
        return 0
    else:
        print("Type not Found")
        return 1
