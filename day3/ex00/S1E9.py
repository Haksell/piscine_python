from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for different types of characters."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Create a new character."""

    @abstractmethod
    def die(self):
        """Kill a character."""


class Stark(Character):
    """A class representing a Stark family member."""

    def __init__(self, first_name, is_alive=True):
        """Create a new Stark family member."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill a Stark family member."""
        self.is_alive = False
