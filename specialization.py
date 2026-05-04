"""
specialization.py
Department / specialization with a priority patient queue.
"""

from patient import Patient


class Specialization:
    """A hospital department that manages its own patient queue."""

    MAX_CAPACITY = 15

    def __init__(self, name: str, head_doctor_id: str = None):
        self._name = name.strip()
        self._head_doctor_id = head_doctor_id
        self._queue: list[Patient] = []
        self._served_count: int = 0

    # ---------- properties ----------
    @property
    def name(self):
        return self._name

    @property
    def head_doctor_id(self):
        return self._head_doctor_id

    @head_doctor_id.setter
    def head_doctor_id(self, doc_id: str):
        self._head_doctor_id = doc_id

    @property
    def queue(self):
        return list(self._queue)

    @property
    def queue_size(self):
        return len(self._queue)

    @property
    def served_count(self):
        return self._served_count

    # ---------- queue operations ----------
    def is_full(self) -> bool:
        return len(self._queue) >= self.MAX_CAPACITY

    def enqueue(self, patient: Patient) -> bool:
        """Add a patient respecting priority order."""
        if self.is_full():
            print(f"  ✗ Queue full for {self._name}.")
            return False
        self._queue.append(patient)
        self._queue.sort(key=lambda p: p.status, reverse=True)
        print(f"  ✓ {patient.name} added to {self._name} [{patient.status_label}]")
        return True

    def dequeue(self) -> Patient | None:
        """Serve and remove the highest-priority patient."""
        if not self._queue:
            print(f"  ✗ No patients in {self._name} queue.")
            return None
        patient = self._queue.pop(0)
        self._served_count += 1
        print(f"  → {patient.name} called to see the doctor.")
        return patient

    def remove_patient(self, patient_id: str) -> bool:
        """Remove a specific patient by ID."""
        for p in self._queue:
            if p.person_id == patient_id:
                self._queue.remove(p)
                print(f"  ✓ {p.name} removed from {self._name} queue.")
                return True
        print(f"  ✗ Patient {patient_id} not found in {self._name}.")
        return False

    def find_patient(self, patient_id: str) -> Patient | None:
        for p in self._queue:
            if p.person_id == patient_id:
                return p
        return None

    def print_queue(self):
        if not self._queue:
            print(f"  (No patients in {self._name})")
            return
        for i, p in enumerate(self._queue, 1):
            print(f"  {i:>2}. {p}")

    def __str__(self):
        return (
            f"Dept: {self._name} | Queue: {len(self._queue)}/{self.MAX_CAPACITY} | "
            f"Served today: {self._served_count}"
        )
