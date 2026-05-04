"""
patient.py
Patient entity — inherits from Person.
"""

from datetime import datetime
from person import Person


class Patient(Person):
    """Represents a hospital patient with medical history and status."""

    STATUS_MAP = {0: "Normal", 1: "Urgent", 2: "Super-Urgent"}
    BLOOD_GROUPS = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}

    def __init__(
        self,
        person_id: str,
        name: str,
        age: int,
        gender: str,
        phone: str,
        blood_group: str,
        status: int = 0,
        allergies: list = None,
    ):
        super().__init__(person_id, name, age, gender, phone)

        if blood_group not in self.BLOOD_GROUPS:
            raise ValueError(f"Invalid blood group: {blood_group}")
        if status not in self.STATUS_MAP:
            raise ValueError("Status must be 0 (Normal), 1 (Urgent) or 2 (Super-Urgent).")

        self._blood_group = blood_group
        self._status = status
        self._allergies: list[str] = allergies or []
        self._medical_history: list[dict] = []
        self._prescriptions: list[dict] = []
        self._registered_at: datetime = datetime.now()
        self._assigned_doctor_id: str | None = None
        self._room_number: str | None = None

    # ---------- properties ----------
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: int):
        if value not in self.STATUS_MAP:
            raise ValueError("Invalid status.")
        self._status = value

    @property
    def status_label(self):
        return self.STATUS_MAP[self._status]

    @property
    def blood_group(self):
        return self._blood_group

    @property
    def allergies(self):
        return list(self._allergies)

    @property
    def medical_history(self):
        return list(self._medical_history)

    @property
    def prescriptions(self):
        return list(self._prescriptions)

    @property
    def registered_at(self):
        return self._registered_at

    @property
    def assigned_doctor_id(self):
        return self._assigned_doctor_id

    @assigned_doctor_id.setter
    def assigned_doctor_id(self, doc_id: str):
        self._assigned_doctor_id = doc_id

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, room: str):
        self._room_number = room

    # ---------- methods ----------
    def add_allergy(self, allergy: str):
        if allergy not in self._allergies:
            self._allergies.append(allergy)

    def add_medical_record(self, diagnosis: str, treatment: str, doctor_name: str):
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "diagnosis": diagnosis,
            "treatment": treatment,
            "doctor": doctor_name,
        }
        self._medical_history.append(record)
        return record

    def add_prescription(self, medicine: str, dosage: str, doctor_name: str, days: int):
        prescription = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "medicine": medicine,
            "dosage": dosage,
            "doctor": doctor_name,
            "duration_days": days,
        }
        self._prescriptions.append(prescription)
        return prescription

    def get_info(self) -> dict:
        info = super().get_info()
        info.update(
            {
                "Blood Group": self._blood_group,
                "Status": self.status_label,
                "Allergies": ", ".join(self._allergies) or "None",
                "Registered At": self._registered_at.strftime("%Y-%m-%d %H:%M"),
                "Assigned Doctor": self._assigned_doctor_id or "Unassigned",
                "Room": self._room_number or "Not admitted",
            }
        )
        return info

    def __str__(self):
        return (
            f"Patient [{self._person_id}] {self._name} | "
            f"Status: {self.status_label} | Blood: {self._blood_group} | "
            f"Age: {self._age}"
        )
