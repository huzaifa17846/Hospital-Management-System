"""
appointment.py
Appointment entity linking Patient ↔ Doctor.
"""

from datetime import datetime


class Appointment:
    """Represents a scheduled consultation between a patient and a doctor."""

    STATUS_OPTIONS = {"scheduled", "completed", "cancelled", "no-show"}

    _counter = 1

    def __init__(
        self,
        patient_id: str,
        doctor_id: str,
        date_str: str,
        time_str: str,
        specialization: str,
        notes: str = "",
    ):
        self._appointment_id = f"APT{Appointment._counter:04d}"
        Appointment._counter += 1
        self._patient_id = patient_id
        self._doctor_id = doctor_id
        self._date = date_str
        self._time = time_str
        self._specialization = specialization
        self._notes = notes
        self._status: str = "scheduled"
        self._created_at: datetime = datetime.now()

    # ---------- properties ----------
    @property
    def appointment_id(self):
        return self._appointment_id

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def doctor_id(self):
        return self._doctor_id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in self.STATUS_OPTIONS:
            raise ValueError(f"Status must be one of: {self.STATUS_OPTIONS}")
        self._status = value

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value: str):
        self._notes = value

    # ---------- methods ----------
    def cancel(self):
        self._status = "cancelled"

    def complete(self):
        self._status = "completed"

    def get_info(self) -> dict:
        return {
            "Appointment ID": self._appointment_id,
            "Patient ID": self._patient_id,
            "Doctor ID": self._doctor_id,
            "Date": self._date,
            "Time": self._time,
            "Specialization": self._specialization,
            "Status": self._status.title(),
            "Notes": self._notes or "None",
        }

    def __str__(self):
        return (
            f"Appt [{self._appointment_id}] {self._date} {self._time} | "
            f"Patient: {self._patient_id} → Dr: {self._doctor_id} | "
            f"{self._specialization} | {self._status.upper()}"
        )
