from typing import Any


def callLimit(limit: int):
    """Wrap function to limit call times."""
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(
                    f"Error: <function {function.__name__} at 0x{id(function):x}>"
                    " call too many times"
                )
                return None

        return limit_function

    return callLimiter
