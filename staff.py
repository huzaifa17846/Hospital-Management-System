"""
staff.py
Non-medical staff entity — inherits from Person.
"""

from person import Person


class Staff(Person):
    """Represents hospital support staff (nurses, receptionists, technicians, etc.)."""

    ROLES = {
        "nurse",
        "receptionist",
        "lab technician",
        "pharmacist",
        "ward boy",
        "administrator",
        "cleaner",
        "security",
    }

    def __init__(
        self,
        person_id: str,
        name: str,
        age: int,
        gender: str,
        phone: str,
        role: str,
        department: str,
        salary: float,
        shift: str = "morning",
    ):
        super().__init__(person_id, name, age, gender, phone)
        if role.lower() not in self.ROLES:
            raise ValueError(f"Invalid role. Choose from: {self.ROLES}")
        self._role = role.lower()
        self._department = department
        self._salary = salary
        self._shift = shift
        self._is_active: bool = True

    # ---------- properties ----------
    @property
    def role(self):
        return self._role

    @property
    def department(self):
        return self._department

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, value: str):
        self._shift = value

    @property
    def is_active(self):
        return self._is_active

    def deactivate(self):
        self._is_active = False

    def activate(self):
        self._is_active = True

    def get_info(self) -> dict:
        info = super().get_info()
        info.update(
            {
                "Role": self._role.title(),
                "Department": self._department,
                "Salary": f"Rs. {self._salary:,.0f}",
                "Shift": self._shift,
                "Active": "Yes" if self._is_active else "No",
            }
        )
        return info

    def __str__(self):
        status = "ACTIVE" if self._is_active else "INACTIVE"
        return (
            f"Staff [{self._person_id}] {self._name} | "
            f"{self._role.title()} | {self._department} | {self._shift} shift | {status}"
        )
