import random
import string
from dataclasses import dataclass, field


@dataclass
class Student:
    """Represent a student."""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Finish the initialization of the object."""
        first_letter_of_name = self.name[0]
        first_seven_letters_of_surname = self.surname[:7]
        login = f"{first_letter_of_name}{first_seven_letters_of_surname}"
        self.login = login.lower()
        self.id = "".join(random.choices(string.ascii_lowercase, k=15))
