def square(x: int | float) -> int | float:
    """Take a number and return its square."""
    return x * x


def pow(x: int | float) -> int | float:
    """Take a number and return its power with itself."""
    return x**x


def outer(x: int | float, function) -> object:
    """Wrap a repeated function call."""

    def inner() -> int | float:
        nonlocal x
        x = function(x)
        return x

    return inner
