class calculator:
    """Represent a calculator on several numbers."""

    def __init__(self, data: list) -> None:
        """Construct a calculator."""
        self.data = data

    def __add__(self, x) -> None:
        """Add a number to all the numbers in the calculator."""
        self.data = [d + x for d in self.data]
        return self.data

    def __mul__(self, x) -> None:
        """Multiply all the numbers in the calculator by a number."""
        self.data = [d * x for d in self.data]
        return self.data

    def __sub__(self, x) -> None:
        """Subtract a number from all the numbers in the calculator."""
        self.data = [d - x for d in self.data]
        return self.data

    def __truediv__(self, x) -> None:
        """Divide all the numbers in the calculator by a number."""
        if x == 0:
            raise ZeroDivisionError(f"trying to divide {self!r} by 0")
        self.data = [d / x for d in self.data]
        return self.data

    def __repr__(self) -> str:
        """Return a debugging representation of the object."""
        return f"calculator({self.data!r})"
