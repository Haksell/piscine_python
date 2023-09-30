from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Create a new Baratheon family member."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill a Baratheon family member."""
        self.is_alive = False

    def __str__(self):
        """Return a displayable representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a debugging representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Create a new Lannister family member."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill a Lannister family member."""
        self.is_alive = False

    def __str__(self):
        """Return a displayable representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a debugging representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a new Lannister family member."""
        return cls(first_name, is_alive)
