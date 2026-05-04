"""
room.py
Hospital Room entity.
"""


class Room:
    """Represents a hospital room or bed unit."""

    ROOM_TYPES = {"general", "private", "icu", "emergency", "operation theatre", "lab"}

    def __init__(self, room_number: str, room_type: str, floor: int, daily_charge: float):
        if room_type.lower() not in self.ROOM_TYPES:
            raise ValueError(f"Room type must be one of: {self.ROOM_TYPES}")
        self._room_number = room_number
        self._room_type = room_type.lower()
        self._floor = floor
        self._daily_charge = daily_charge
        self._is_occupied: bool = False
        self._patient_id: str | None = None
        self._admitted_date: str | None = None

    # ---------- properties ----------
    @property
    def room_number(self):
        return self._room_number

    @property
    def room_type(self):
        return self._room_type

    @property
    def floor(self):
        return self._floor

    @property
    def daily_charge(self):
        return self._daily_charge

    @property
    def is_occupied(self):
        return self._is_occupied

    @property
    def patient_id(self):
        return self._patient_id

    # ---------- methods ----------
    def admit_patient(self, patient_id: str, date_str: str):
        if self._is_occupied:
            raise RuntimeError(f"Room {self._room_number} is already occupied.")
        self._is_occupied = True
        self._patient_id = patient_id
        self._admitted_date = date_str

    def discharge_patient(self):
        if not self._is_occupied:
            raise RuntimeError(f"Room {self._room_number} is already empty.")
        self._is_occupied = False
        self._patient_id = None
        self._admitted_date = None

    def get_info(self) -> dict:
        return {
            "Room No": self._room_number,
            "Type": self._room_type.title(),
            "Floor": self._floor,
            "Daily Charge": f"Rs. {self._daily_charge:,.0f}",
            "Status": "Occupied" if self._is_occupied else "Available",
            "Patient ID": self._patient_id or "—",
        }

    def __str__(self):
        status = f"OCCUPIED by {self._patient_id}" if self._is_occupied else "AVAILABLE"
        return (
            f"Room {self._room_number} | {self._room_type.title()} | "
            f"Floor {self._floor} | Rs.{self._daily_charge:,.0f}/day | {status}"
        )
