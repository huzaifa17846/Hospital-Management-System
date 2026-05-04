"""
main.py
Entry point — full interactive CLI for the Hospital Management System.
"""

from hospital import Hospital
from data_seeder import seed


# ─────────────────────────────── helpers ────────────────────────────────────

def separator(char="─", width=55):
    print(char * width)

def header(title: str):
    separator("═")
    print(f"  {title.upper()}")
    separator("═")

def prompt_int(msg: str, lo: int, hi: int) -> int:
    while True:
        try:
            val = int(input(f"  {msg}: "))
            if lo <= val <= hi:
                return val
            print(f"  Please enter a number between {lo} and {hi}.")
        except ValueError:
            print("  Invalid input — enter a number.")

def prompt_str(msg: str) -> str:
    while True:
        val = input(f"  {msg}: ").strip()
        if val:
            return val
        print("  Input cannot be empty.")

def print_dict(d: dict):
    for k, v in d.items():
        print(f"    {k:<22}: {v}")

def pause():
    input("\n  Press Enter to continue...")


# ─────────────────────────────── menus ──────────────────────────────────────

def menu_patients(h: Hospital):
    while True:
        header("Patient Management")
        options = [
            "1) Register new patient",
            "2) List all patients",
            "3) View patient details",
            "4) Search patient by name",
            "5) Admit patient to room",
            "6) Discharge patient",
            "7) Add medical record",
            "8) Add prescription",
            "9) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            name   = prompt_str("Full name")
            age    = prompt_int("Age", 0, 130)
            gender = prompt_str("Gender (Male/Female/Other)")
            phone  = prompt_str("Phone")
            bg     = prompt_str("Blood group (A+/A-/B+/B-/AB+/AB-/O+/O-)")
            st     = prompt_int("Status (0=Normal, 1=Urgent, 2=Super-Urgent)", 0, 2)
            try:
                p = h.add_patient(name, age, gender, phone, bg, st)
                print(f"\n  ✓ Registered: {p}")
            except ValueError as e:
                print(f"\n  ✗ Error: {e}")

        elif choice == 2:
            print()
            h.list_patients()

        elif choice == 3:
            pid = prompt_str("Patient ID (e.g. PAT0001)")
            p = h.get_patient(pid)
            if p:
                print()
                print_dict(p.get_info())
                if p.medical_history:
                    print(f"\n    Medical History ({len(p.medical_history)} records):")
                    for rec in p.medical_history:
                        print(f"      [{rec['date']}] {rec['diagnosis']} — {rec['treatment']} (Dr. {rec['doctor']})")
                if p.prescriptions:
                    print(f"\n    Prescriptions ({len(p.prescriptions)}):")
                    for rx in p.prescriptions:
                        print(f"      [{rx['date']}] {rx['medicine']} {rx['dosage']} for {rx['duration_days']} days (Dr. {rx['doctor']})")
            else:
                print(f"\n  ✗ Patient {pid} not found.")

        elif choice == 4:
            name = prompt_str("Name to search")
            results = h.find_patients_by_name(name)
            if results:
                for p in results:
                    print(f"  {p}")
            else:
                print("  No matching patients.")

        elif choice == 5:
            pid  = prompt_str("Patient ID")
            room = prompt_str("Room number (e.g. R201)")
            h.admit_patient_to_room(pid, room)

        elif choice == 6:
            pid = prompt_str("Patient ID")
            h.discharge_patient(pid)

        elif choice == 7:
            pid   = prompt_str("Patient ID")
            p = h.get_patient(pid)
            if p:
                diag  = prompt_str("Diagnosis")
                treat = prompt_str("Treatment")
                doc   = prompt_str("Doctor name")
                rec   = p.add_medical_record(diag, treat, doc)
                print(f"  ✓ Record added: {rec}")
            else:
                print("  ✗ Patient not found.")

        elif choice == 8:
            pid  = prompt_str("Patient ID")
            p = h.get_patient(pid)
            if p:
                med  = prompt_str("Medicine name")
                dos  = prompt_str("Dosage")
                doc  = prompt_str("Doctor name")
                days = prompt_int("Duration (days)", 1, 365)
                rx   = p.add_prescription(med, dos, doc, days)
                print(f"  ✓ Prescription added: {rx}")
            else:
                print("  ✗ Patient not found.")

        else:
            break

        pause()


def menu_doctors(h: Hospital):
    while True:
        header("Doctor Management")
        options = [
            "1) Register new doctor",
            "2) List all doctors",
            "3) View doctor details",
            "4) Find doctors by specialization",
            "5) Assign doctor to patient",
            "6) Update doctor availability",
            "7) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            name   = prompt_str("Full name (without Dr.)")
            age    = prompt_int("Age", 25, 80)
            gender = prompt_str("Gender")
            phone  = prompt_str("Phone")
            spec   = prompt_str("Specialization")
            qual   = prompt_str("Qualification (e.g. MBBS, FCPS)")
            exp    = prompt_int("Experience (years)", 0, 50)
            fee    = float(prompt_str("Consultation fee (Rs.)"))
            d = h.add_doctor(name, age, gender, phone, spec, qual, exp, fee)
            print(f"\n  ✓ Registered: {d}")

        elif choice == 2:
            print()
            h.list_doctors()

        elif choice == 3:
            did = prompt_str("Doctor ID (e.g. DOC0001)")
            d = h.get_doctor(did)
            if d:
                print()
                print_dict(d.get_info())
                if d.appointments:
                    print(f"\n    Appointments ({len(d.appointments)}):")
                    for a in d.appointments:
                        print(f"      [{a['date']}] Patient {a['patient_id']} — {a['status']}")
            else:
                print(f"\n  ✗ Doctor {did} not found.")

        elif choice == 4:
            spec = prompt_str("Specialization keyword")
            results = h.find_doctors_by_specialization(spec)
            if results:
                for d in results:
                    print(f"  {d}")
            else:
                print("  No matching doctors.")

        elif choice == 5:
            did = prompt_str("Doctor ID")
            pid = prompt_str("Patient ID")
            h.assign_doctor_to_patient(did, pid)

        elif choice == 6:
            did = prompt_str("Doctor ID")
            d = h.get_doctor(did)
            if d:
                print("  Statuses: available / busy / off-duty / on-leave")
                status = prompt_str("New status")
                try:
                    d.availability = status
                    print(f"  ✓ {d.name} is now {status}.")
                except ValueError as e:
                    print(f"  ✗ {e}")
            else:
                print("  ✗ Doctor not found.")

        else:
            break

        pause()


def menu_rooms(h: Hospital):
    while True:
        header("Room Management")
        options = [
            "1) List all rooms",
            "2) List available rooms",
            "3) View room details",
            "4) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            print()
            h.list_rooms()
        elif choice == 2:
            print()
            h.list_rooms(only_available=True)
        elif choice == 3:
            rno = prompt_str("Room number (e.g. ICU1)")
            r = h.get_room(rno)
            if r:
                print()
                print_dict(r.get_info())
            else:
                print("  ✗ Room not found.")
        else:
            break

        pause()


def menu_appointments(h: Hospital):
    while True:
        header("Appointments")
        options = [
            "1) Book appointment",
            "2) List all appointments",
            "3) List appointments for a patient",
            "4) Cancel / complete appointment",
            "5) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            pid   = prompt_str("Patient ID")
            did   = prompt_str("Doctor ID")
            date  = prompt_str("Date (YYYY-MM-DD)")
            time  = prompt_str("Time (HH:MM)")
            notes = input("  Notes (optional): ").strip()
            h.book_appointment(pid, did, date, time, notes)

        elif choice == 2:
            print()
            h.list_appointments()

        elif choice == 3:
            pid = prompt_str("Patient ID")
            print()
            h.list_appointments(patient_id=pid)

        elif choice == 4:
            aid = prompt_str("Appointment ID (e.g. APT0001)")
            a = h.get_appointment(aid)
            if a:
                print(f"  Current status: {a.status}")
                action = prompt_str("Action (cancel / complete)")
                if action == "cancel":
                    a.cancel()
                    print("  ✓ Appointment cancelled.")
                elif action == "complete":
                    a.complete()
                    print("  ✓ Appointment marked complete.")
                else:
                    print("  ✗ Unknown action.")
            else:
                print("  ✗ Appointment not found.")

        else:
            break

        pause()


def menu_queues(h: Hospital):
    while True:
        header("Patient Queues")
        options = [
            "1) View all queues",
            "2) Add patient to queue",
            "3) Call next patient",
            "4) Remove patient from queue",
            "5) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            h.list_queues()

        elif choice == 2:
            pid  = prompt_str("Patient ID")
            spec = prompt_str("Specialization (e.g. Cardiology)")
            h.add_patient_to_queue(pid, spec)

        elif choice == 3:
            spec = prompt_str("Specialization")
            p = h.call_next_patient(spec)
            if p:
                print(f"\n  Patient called: {p}")

        elif choice == 4:
            spec = prompt_str("Specialization")
            s = h.get_specialization(spec)
            if s:
                pid = prompt_str("Patient ID to remove")
                s.remove_patient(pid)
            else:
                print("  ✗ Specialization not found.")

        else:
            break

        pause()


def menu_billing(h: Hospital):
    while True:
        header("Billing")
        options = [
            "1) Create bill for patient",
            "2) Add item to bill",
            "3) Print bill",
            "4) Mark bill as paid",
            "5) List all bills",
            "6) List unpaid bills",
            "7) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            pid = prompt_str("Patient ID")
            h.create_bill(pid)

        elif choice == 2:
            bid  = prompt_str("Bill ID (e.g. BILL0001)")
            b = h.get_bill(bid)
            if b:
                desc = prompt_str("Item description")
                amt  = float(prompt_str("Amount (Rs.)"))
                qty  = prompt_int("Quantity", 1, 999)
                b.add_item(desc, amt, qty)
                disc = float(input("  Discount % (0 to skip): ") or 0)
                if disc:
                    b.discount_percent = disc
                print(f"  ✓ Item added. Running total: Rs. {b.total:,.0f}")
            else:
                print("  ✗ Bill not found.")

        elif choice == 3:
            bid = prompt_str("Bill ID")
            b = h.get_bill(bid)
            if b:
                b.print_bill()
            else:
                print("  ✗ Bill not found.")

        elif choice == 4:
            bid = prompt_str("Bill ID")
            b = h.get_bill(bid)
            if b:
                b.pay()
                print("  ✓ Bill marked as paid.")
            else:
                print("  ✗ Bill not found.")

        elif choice == 5:
            print()
            h.list_bills()

        elif choice == 6:
            print()
            h.list_bills(only_unpaid=True)

        else:
            break

        pause()


def menu_staff(h: Hospital):
    while True:
        header("Staff Management")
        options = [
            "1) Register new staff member",
            "2) List all staff",
            "3) View staff details",
            "4) Back to main menu",
        ]
        print("\n".join(f"  {o}" for o in options))
        choice = prompt_int("Choice", 1, len(options))

        if choice == 1:
            name  = prompt_str("Full name")
            age   = prompt_int("Age", 18, 70)
            gender= prompt_str("Gender")
            phone = prompt_str("Phone")
            role  = prompt_str("Role (nurse/receptionist/lab technician/pharmacist/ward boy/administrator/cleaner/security)")
            dept  = prompt_str("Department")
            sal   = float(prompt_str("Salary (Rs.)"))
            shift = prompt_str("Shift (morning/evening/night)")
            try:
                s = h.add_staff(name, age, gender, phone, role, dept, sal, shift)
                print(f"\n  ✓ Registered: {s}")
            except ValueError as e:
                print(f"\n  ✗ Error: {e}")

        elif choice == 2:
            print()
            h.list_staff()

        elif choice == 3:
            sid = prompt_str("Staff ID (e.g. STF0001)")
            s = h.get_staff(sid)
            if s:
                print()
                print_dict(s.get_info())
            else:
                print("  ✗ Staff member not found.")

        else:
            break

        pause()


# ─────────────────────────────── main ───────────────────────────────────────

def main():
    h = Hospital(
        name="City General Hospital",
        address="12-A, Medical Road, Rawalpindi, Punjab",
        contact="+92-51-1234567",
    )

    print("\n" + "═" * 55)
    print("   CITY GENERAL HOSPITAL — Management System")
    print("═" * 55)
    print("  Loading sample data...")
    seed(h)

    main_menu = [
        "1) Patient Management",
        "2) Doctor Management",
        "3) Staff Management",
        "4) Room Management",
        "5) Appointments",
        "6) Patient Queues",
        "7) Billing",
        "8) Daily Summary",
        "9) Exit",
    ]

    while True:
        header("Main Menu")
        print(f"\n  {h}\n")
        print("\n".join(f"  {o}" for o in main_menu))
        choice = prompt_int("Choice", 1, len(main_menu))

        if choice == 1:
            menu_patients(h)
        elif choice == 2:
            menu_doctors(h)
        elif choice == 3:
            menu_staff(h)
        elif choice == 4:
            menu_rooms(h)
        elif choice == 5:
            menu_appointments(h)
        elif choice == 6:
            menu_queues(h)
        elif choice == 7:
            menu_billing(h)
        elif choice == 8:
            h.daily_summary()
            pause()
        else:
            print("\n  Goodbye! Stay healthy. 🏥\n")
            break


if __name__ == "__main__":
    main()
