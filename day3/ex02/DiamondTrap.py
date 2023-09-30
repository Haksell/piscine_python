from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing Joffrey Baratheon."""

    def __init__(self, first_name, is_alive=True):
        """Create a new King."""
        super().__init__(first_name, is_alive)
        self.family_name = self.__class__.__mro__[1].__name__

    def set_eyes(self, color):
        """Setter for eyes."""
        self.eyes = color

    def get_eyes(self):
        """Getter for eyes."""
        return self.eyes

    def set_hairs(self, color):
        """Setter for hairs."""
        self.hairs = color

    def get_hairs(self):
        """Getter for hairs."""
        return self.hairs
