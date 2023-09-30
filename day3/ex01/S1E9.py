from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for different types of characters."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Create a new character."""

    @abstractmethod
    def die(self):
        """Kill a character."""

    @abstractmethod
    def __str__(self):
        """Return a displayable representation of the object."""

    @abstractmethod
    def __repr__(self):
        """Return a debugging representation of the object."""


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """Create a new Stark family member."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = "grey"
        self.hairs = "brown"

    def die(self):
        """Kill a Stark family member."""
        self.is_alive = False

    def __str__(self):
        """Return a displayable representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a debugging representation of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
