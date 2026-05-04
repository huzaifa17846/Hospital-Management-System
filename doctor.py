"""
doctor.py
Doctor entity — inherits from Person.
"""

from datetime import datetime
from person import Person


class Doctor(Person):
    """Represents a hospital doctor with specialization and schedule."""

    AVAILABILITY = {"available", "busy", "off-duty", "on-leave"}

    def __init__(
        self,
        person_id: str,
        name: str,
        age: int,
        gender: str,
        phone: str,
        specialization: str,
        qualification: str,
        experience_years: int,
        consultation_fee: float,
    ):
        super().__init__(person_id, name, age, gender, phone)
        self._specialization = specialization
        self._qualification = qualification
        self._experience_years = experience_years
        self._consultation_fee = consultation_fee
        self._availability: str = "available"
        self._patient_ids: list[str] = []
        self._appointments: list[dict] = []
        self._joined_date: datetime = datetime.now()

    # ---------- properties ----------
    @property
    def specialization(self):
        return self._specialization

    @property
    def qualification(self):
        return self._qualification

    @property
    def experience_years(self):
        return self._experience_years

    @property
    def consultation_fee(self):
        return self._consultation_fee

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value: str):
        if value not in self.AVAILABILITY:
            raise ValueError(f"Availability must be one of: {self.AVAILABILITY}")
        self._availability = value

    @property
    def patient_ids(self):
        return list(self._patient_ids)

    @property
    def appointments(self):
        return list(self._appointments)

    # ---------- methods ----------
    def assign_patient(self, patient_id: str):
        if patient_id not in self._patient_ids:
            self._patient_ids.append(patient_id)

    def release_patient(self, patient_id: str):
        if patient_id in self._patient_ids:
            self._patient_ids.remove(patient_id)

    def add_appointment(self, patient_id: str, date_str: str, notes: str = ""):
        appt = {
            "patient_id": patient_id,
            "date": date_str,
            "notes": notes,
            "status": "scheduled",
        }
        self._appointments.append(appt)
        return appt

    def complete_appointment(self, patient_id: str):
        for appt in self._appointments:
            if appt["patient_id"] == patient_id and appt["status"] == "scheduled":
                appt["status"] = "completed"
                return True
        return False

    def get_info(self) -> dict:
        info = super().get_info()
        info.update(
            {
                "Specialization": self._specialization,
                "Qualification": self._qualification,
                "Experience": f"{self._experience_years} years",
                "Consultation Fee": f"Rs. {self._consultation_fee:,.0f}",
                "Availability": self._availability,
                "Patients Assigned": len(self._patient_ids),
            }
        )
        return info

    def __str__(self):
        display_name = self._name if self._name.startswith("Dr.") else f"Dr. {self._name}"
        return (
            f"{display_name} [{self._person_id}] | "
            f"{self._specialization} | {self._qualification} | "
            f"{self._experience_years} yrs exp | {self._availability.upper()}"
        )
