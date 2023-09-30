from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for different types of characters."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Create a new character."""
        pass

    @abstractmethod
    def die():
        """Kill the character."""
        pass


class Stark(Character):
    """A class representing the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """Create a new Stark character."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill a Stark."""
        self.is_alive = False
