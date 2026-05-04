"""
hospital.py
The Hospital class — central registry for all entities.
"""

from datetime import datetime

from patient import Patient
from doctor import Doctor
from staff import Staff
from room import Room
from appointment import Appointment
from bill import Bill
from specialization import Specialization


class Hospital:
    """
    Top-level class that owns and manages:
    Patients, Doctors, Staff, Rooms, Appointments, Bills, Specializations.
    """

    def __init__(self, name: str, address: str, contact: str):
        self._name = name
        self._address = address
        self._contact = contact
        self._established = datetime.now().year

        # Registries
        self._patients: dict[str, Patient] = {}
        self._doctors: dict[str, Doctor] = {}
        self._staff: dict[str, Staff] = {}
        self._rooms: dict[str, Room] = {}
        self._appointments: dict[str, Appointment] = {}
        self._bills: dict[str, Bill] = {}
        self._specializations: dict[str, Specialization] = {}

        # Auto-increment counters for IDs
        self._patient_ctr = 1
        self._doctor_ctr = 1
        self._staff_ctr = 1

    # ─────────────────────────────── properties ────────────────────────────
    @property
    def name(self):
        return self._name

    # ═══════════════════════════ PATIENT ════════════════════════════════════
    def _next_patient_id(self):
        pid = f"PAT{self._patient_ctr:04d}"
        self._patient_ctr += 1
        return pid

    def add_patient(self, name, age, gender, phone, blood_group, status=0, allergies=None) -> Patient:
        pid = self._next_patient_id()
        p = Patient(pid, name, age, gender, phone, blood_group, status, allergies)
        self._patients[pid] = p
        return p

    def get_patient(self, patient_id: str) -> Patient | None:
        return self._patients.get(patient_id)

    def find_patients_by_name(self, name: str) -> list[Patient]:
        name_lower = name.lower()
        return [p for p in self._patients.values() if name_lower in p.name.lower()]

    def discharge_patient(self, patient_id: str):
        p = self._patients.get(patient_id)
        if not p:
            print(f"  ✗ Patient {patient_id} not found.")
            return
        if p.room_number:
            room = self._rooms.get(p.room_number)
            if room:
                room.discharge_patient()
            p.room_number = None
        if p.assigned_doctor_id:
            doc = self._doctors.get(p.assigned_doctor_id)
            if doc:
                doc.release_patient(patient_id)
            p.assigned_doctor_id = None
        print(f"  ✓ Patient {p.name} discharged.")

    def list_patients(self):
        if not self._patients:
            print("  No patients registered.")
            return
        for p in self._patients.values():
            print(f"  {p}")

    # ═══════════════════════════ DOCTOR ═════════════════════════════════════
    def _next_doctor_id(self):
        did = f"DOC{self._doctor_ctr:04d}"
        self._doctor_ctr += 1
        return did

    def add_doctor(self, name, age, gender, phone, specialization, qualification, experience, fee) -> Doctor:
        did = self._next_doctor_id()
        d = Doctor(did, name, age, gender, phone, specialization, qualification, experience, fee)
        self._doctors[did] = d
        # Auto-create specialization dept if it doesn't exist
        if specialization not in self._specializations:
            self._specializations[specialization] = Specialization(specialization, did)
        return d

    def get_doctor(self, doctor_id: str) -> Doctor | None:
        return self._doctors.get(doctor_id)

    def find_doctors_by_specialization(self, spec: str) -> list[Doctor]:
        return [d for d in self._doctors.values() if spec.lower() in d.specialization.lower()]

    def list_doctors(self):
        if not self._doctors:
            print("  No doctors registered.")
            return
        for d in self._doctors.values():
            print(f"  {d}")

    def assign_doctor_to_patient(self, doctor_id: str, patient_id: str):
        doc = self._doctors.get(doctor_id)
        pat = self._patients.get(patient_id)
        if not doc:
            print(f"  ✗ Doctor {doctor_id} not found.")
            return False
        if not pat:
            print(f"  ✗ Patient {patient_id} not found.")
            return False
        doc.assign_patient(patient_id)
        pat.assigned_doctor_id = doctor_id
        print(f"  ✓ Dr. {doc.name} assigned to {pat.name}.")
        return True

    # ═══════════════════════════ STAFF ══════════════════════════════════════
    def _next_staff_id(self):
        sid = f"STF{self._staff_ctr:04d}"
        self._staff_ctr += 1
        return sid

    def add_staff(self, name, age, gender, phone, role, department, salary, shift="morning") -> Staff:
        sid = self._next_staff_id()
        s = Staff(sid, name, age, gender, phone, role, department, salary, shift)
        self._staff[sid] = s
        return s

    def get_staff(self, staff_id: str) -> Staff | None:
        return self._staff.get(staff_id)

    def list_staff(self):
        if not self._staff:
            print("  No staff registered.")
            return
        for s in self._staff.values():
            print(f"  {s}")

    # ═══════════════════════════ ROOMS ══════════════════════════════════════
    def add_room(self, room_number, room_type, floor, daily_charge) -> Room:
        r = Room(room_number, room_type, floor, daily_charge)
        self._rooms[room_number] = r
        return r

    def get_room(self, room_number: str) -> Room | None:
        return self._rooms.get(room_number)

    def admit_patient_to_room(self, patient_id: str, room_number: str):
        room = self._rooms.get(room_number)
        pat = self._patients.get(patient_id)
        if not room:
            print(f"  ✗ Room {room_number} not found.")
            return False
        if not pat:
            print(f"  ✗ Patient {patient_id} not found.")
            return False
        if room.is_occupied:
            print(f"  ✗ Room {room_number} is occupied.")
            return False
        date_str = datetime.now().strftime("%Y-%m-%d")
        room.admit_patient(patient_id, date_str)
        pat.room_number = room_number
        print(f"  ✓ {pat.name} admitted to Room {room_number}.")
        return True

    def list_rooms(self, only_available=False):
        rooms = [r for r in self._rooms.values() if not only_available or not r.is_occupied]
        if not rooms:
            print("  No rooms found.")
            return
        for r in rooms:
            print(f"  {r}")

    # ═══════════════════════════ APPOINTMENTS ═══════════════════════════════
    def book_appointment(self, patient_id, doctor_id, date_str, time_str, notes="") -> Appointment | None:
        doc = self._doctors.get(doctor_id)
        pat = self._patients.get(patient_id)
        if not doc or not pat:
            print("  ✗ Invalid patient or doctor ID.")
            return None
        appt = Appointment(patient_id, doctor_id, date_str, time_str, doc.specialization, notes)
        self._appointments[appt.appointment_id] = appt
        doc.add_appointment(patient_id, date_str, notes)
        print(f"  ✓ Appointment {appt.appointment_id} booked: {pat.name} → Dr. {doc.name} on {date_str}.")
        return appt

    def get_appointment(self, appt_id: str) -> Appointment | None:
        return self._appointments.get(appt_id)

    def list_appointments(self, patient_id: str = None):
        appts = self._appointments.values()
        if patient_id:
            appts = [a for a in appts if a.patient_id == patient_id]
        if not appts:
            print("  No appointments found.")
            return
        for a in appts:
            print(f"  {a}")

    # ═══════════════════════════ BILLING ════════════════════════════════════
    def create_bill(self, patient_id: str) -> Bill | None:
        pat = self._patients.get(patient_id)
        if not pat:
            print(f"  ✗ Patient {patient_id} not found.")
            return None
        bill = Bill(patient_id, pat.name)
        self._bills[bill.bill_id] = bill
        print(f"  ✓ Bill {bill.bill_id} created for {pat.name}.")
        return bill

    def get_bill(self, bill_id: str) -> Bill | None:
        return self._bills.get(bill_id)

    def list_bills(self, only_unpaid=False):
        bills = [b for b in self._bills.values() if not only_unpaid or not b.is_paid]
        if not bills:
            print("  No bills found.")
            return
        for b in bills:
            print(f"  {b}")

    # ═══════════════════════════ SPECIALIZATIONS / QUEUES ═══════════════════
    def get_specialization(self, name: str) -> Specialization | None:
        return self._specializations.get(name)

    def add_patient_to_queue(self, patient_id: str, spec_name: str) -> bool:
        pat = self._patients.get(patient_id)
        if not pat:
            print(f"  ✗ Patient {patient_id} not found.")
            return False
        if spec_name not in self._specializations:
            self._specializations[spec_name] = Specialization(spec_name)
        return self._specializations[spec_name].enqueue(pat)

    def call_next_patient(self, spec_name: str) -> Patient | None:
        spec = self._specializations.get(spec_name)
        if not spec:
            print(f"  ✗ Specialization '{spec_name}' not found.")
            return None
        return spec.dequeue()

    def list_queues(self):
        if not self._specializations:
            print("  No specializations.")
            return
        for s in self._specializations.values():
            print(f"\n  {s}")
            s.print_queue()

    # ═══════════════════════════ REPORTS ════════════════════════════════════
    def daily_summary(self):
        total_rooms = len(self._rooms)
        occupied = sum(1 for r in self._rooms.values() if r.is_occupied)
        unpaid_bills = sum(1 for b in self._bills.values() if not b.is_paid)
        unpaid_total = sum(b.total for b in self._bills.values() if not b.is_paid)
        scheduled_appts = sum(1 for a in self._appointments.values() if a.status == "scheduled")

        print(f"\n{'═'*55}")
        print(f"  DAILY SUMMARY — {self._name}")
        print(f"{'═'*55}")
        print(f"  Patients   : {len(self._patients)}")
        print(f"  Doctors    : {len(self._doctors)}")
        print(f"  Staff      : {len(self._staff)}")
        print(f"  Rooms      : {occupied}/{total_rooms} occupied")
        print(f"  Appts      : {scheduled_appts} scheduled")
        print(f"  Unpaid Bills: {unpaid_bills}  (Rs. {unpaid_total:,.0f})")
        for spec in self._specializations.values():
            print(f"  Queue [{spec.name}]: {spec.queue_size} waiting")
        print(f"{'═'*55}\n")

    def __str__(self):
        return (
            f"🏥 {self._name} | {self._address} | {self._contact}\n"
            f"   Patients: {len(self._patients)} | Doctors: {len(self._doctors)} | "
            f"Staff: {len(self._staff)} | Rooms: {len(self._rooms)}"
        )
