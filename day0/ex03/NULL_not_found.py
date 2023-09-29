import typing


def NULL_not_found(obj: typing.Any) -> int:
    """Print the type of falsy objects."""
    if not obj:
        title = (
            "Nothing"
            if obj is None
            else "Fake"
            if obj is False
            else "Zero"
            if obj == 0
            else "Empty"
        )
    elif type(obj) is float and obj != obj:
        title = "Cheese"
    else:
        print("Type not Found")
        return 1
    print(f"{title}: {obj} {type(obj)}")
    return 0
