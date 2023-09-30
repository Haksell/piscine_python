class calculator:
    """Calculator class."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product between 2 vectors."""
        res = sum(x1 * x2 for x1, x2 in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add 2 vectors."""
        res = [float(x1 + x2) for x1, x2 in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract 2 vectors."""
        res = [float(x1 - x2) for x1, x2 in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
