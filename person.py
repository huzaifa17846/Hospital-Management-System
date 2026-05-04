"""
person.py
Base class for all human entities in the hospital system.
"""


class Person:
    """Abstract base representing any person in the hospital."""

    def __init__(self, person_id: str, name: str, age: int, gender: str, phone: str):
        self._person_id = person_id
        self._name = name
        self._age = age
        self._gender = gender
        self._phone = phone

    # ---------- properties ----------
    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if not (0 <= value <= 130):
            raise ValueError("Age must be between 0 and 130.")
        self._age = value

    @property
    def gender(self):
        return self._gender

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value: str):
        self._phone = value

    # ---------- dunder ----------
    def __str__(self):
        return f"[{self._person_id}] {self._name} | Age: {self._age} | {self._gender} | Phone: {self._phone}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self._person_id!r}, name={self._name!r})"

    def get_info(self) -> dict:
        """Return a dictionary of personal details."""
        return {
            "ID": self._person_id,
            "Name": self._name,
            "Age": self._age,
            "Gender": self._gender,
            "Phone": self._phone,
        }
