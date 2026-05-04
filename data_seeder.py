"""
data_seeder.py
Generates realistic sample data to pre-populate the hospital system.
"""

from hospital import Hospital


def seed(hospital: Hospital):
    """Populate the hospital with doctors, staff, rooms, patients, appointments, and bills."""

    h = hospital

    # ──────────────────────── ROOMS ─────────────────────────────────────────
    rooms_data = [
        ("R101", "general",           1, 2500),
        ("R102", "general",           1, 2500),
        ("R103", "general",           1, 2500),
        ("R201", "private",           2, 6000),
        ("R202", "private",           2, 6000),
        ("R203", "private",           2, 6000),
        ("ICU1", "icu",               3, 15000),
        ("ICU2", "icu",               3, 15000),
        ("ICU3", "icu",               3, 15000),
        ("ER01", "emergency",         0, 5000),
        ("ER02", "emergency",         0, 5000),
        ("OT01", "operation theatre", 3, 25000),
        ("OT02", "operation theatre", 3, 25000),
        ("LAB1", "lab",               1, 1000),
    ]
    for rn, rt, fl, dc in rooms_data:
        h.add_room(rn, rt, fl, dc)

    # ──────────────────────── DOCTORS ───────────────────────────────────────
    doctors_data = [
        ("Dr. Ayesha Tariq",    45, "Female", "0300-1112233", "Cardiology",       "MBBS, FCPS",     18, 3000),
        ("Dr. Bilal Hassan",    38, "Male",   "0300-2223344", "Cardiology",       "MBBS, MD",       12, 2500),
        ("Dr. Sara Malik",      50, "Female", "0301-3334455", "Neurology",        "MBBS, FCPS",     22, 3500),
        ("Dr. Usman Raza",      42, "Male",   "0301-4445566", "Neurology",        "MBBS, PhD",      15, 3200),
        ("Dr. Nadia Khan",      36, "Female", "0302-5556677", "Orthopedics",      "MBBS, MS",       10, 2800),
        ("Dr. Farhan Ahmed",    48, "Male",   "0302-6667788", "Orthopedics",      "MBBS, FRCS",     20, 3000),
        ("Dr. Zara Qureshi",    33, "Female", "0303-7778899", "Pediatrics",       "MBBS, DCH",       8, 2000),
        ("Dr. Kamran Iqbal",    55, "Male",   "0303-8889900", "General Surgery",  "MBBS, FRCS",     28, 4000),
        ("Dr. Amna Siddiqui",   40, "Female", "0304-9990011", "Dermatology",      "MBBS, MCPS",     14, 2200),
        ("Dr. Hamid Qazi",      44, "Male",   "0304-0001122", "Ophthalmology",    "MBBS, DOMS",     16, 2500),
        ("Dr. Rabia Javed",     37, "Female", "0305-1112233", "Gynecology",       "MBBS, FCPS",     11, 3000),
        ("Dr. Tariq Mehmood",   52, "Male",   "0305-2223344", "ENT",              "MBBS, MS",       24, 2800),
    ]
    doctor_objs = []
    for row in doctors_data:
        d = h.add_doctor(*row)
        doctor_objs.append(d)

    # ──────────────────────── STAFF ─────────────────────────────────────────
    staff_data = [
        ("Maria Joseph",    30, "Female", "0311-1010101", "nurse",          "Cardiology",      45000, "morning"),
        ("Asad Butt",       28, "Male",   "0311-2020202", "nurse",          "Neurology",       45000, "evening"),
        ("Saba Noor",       25, "Female", "0311-3030303", "receptionist",   "Reception",       35000, "morning"),
        ("Khalid Mehmood",  35, "Male",   "0311-4040404", "lab technician", "Laboratory",      50000, "morning"),
        ("Hina Baig",       29, "Female", "0311-5050505", "pharmacist",     "Pharmacy",        55000, "morning"),
        ("Imran Ali",       40, "Male",   "0311-6060606", "administrator",  "Administration",  70000, "morning"),
        ("Noman Sher",      22, "Male",   "0311-7070707", "ward boy",       "General Ward",    25000, "night"),
        ("Fatima Sheikh",   27, "Female", "0311-8080808", "nurse",          "ICU",             50000, "night"),
        ("Zeeshan Mir",     33, "Male",   "0311-9090909", "security",       "Security",        28000, "morning"),
        ("Lubna Rashid",    31, "Female", "0311-0000001", "pharmacist",     "Pharmacy",        55000, "evening"),
    ]
    for row in staff_data:
        h.add_staff(*row)

    # ──────────────────────── PATIENTS ──────────────────────────────────────
    patients_data = [
        # name,               age, gender,   phone,          blood, status, allergies
        ("Ahmed Nawaz",        55, "Male",   "0321-1111111", "B+",  2,  ["Penicillin"]),
        ("Fatima Bibi",        34, "Female", "0321-2222222", "A+",  1,  []),
        ("Rahim Shah",         70, "Male",   "0321-3333333", "O+",  2,  ["Aspirin", "Sulfa"]),
        ("Sana Akbar",         25, "Female", "0321-4444444", "AB+", 0,  []),
        ("Tahir Hussain",      45, "Male",   "0321-5555555", "B-",  1,  ["NSAIDs"]),
        ("Nazia Parveen",      30, "Female", "0321-6666666", "O-",  0,  []),
        ("Shahid Latif",       60, "Male",   "0321-7777777", "A-",  2,  []),
        ("Razia Sultana",      48, "Female", "0321-8888888", "AB-", 1,  ["Latex"]),
        ("Usman Farooq",       22, "Male",   "0321-9999999", "B+",  0,  []),
        ("Maryam Khalid",      38, "Female", "0322-1111111", "A+",  1,  ["Codeine"]),
        ("Junaid Baig",        50, "Male",   "0322-2222222", "O+",  0,  []),
        ("Bushra Naz",         29, "Female", "0322-3333333", "B+",  0,  []),
        ("Kamran Yousaf",      65, "Male",   "0322-4444444", "A+",  2,  ["Morphine"]),
        ("Rubina Siddiq",      42, "Female", "0322-5555555", "O+",  1,  []),
        ("Ali Hassan",          8, "Male",   "0322-6666666", "B-",  0,  []),
        ("Zainab Iqbal",       19, "Female", "0322-7777777", "AB+", 0,  []),
        ("Hassan Mahmood",     73, "Male",   "0322-8888888", "O-",  2,  ["Warfarin"]),
        ("Shazia Anwar",       35, "Female", "0322-9999999", "A-",  1,  []),
        ("Nadeem Ul Haq",      44, "Male",   "0323-1111111", "B+",  0,  []),
        ("Samina Tariq",       27, "Female", "0323-2222222", "A+",  0,  []),
    ]
    patient_objs = []
    for row in patients_data:
        p = h.add_patient(*row)
        patient_objs.append(p)

    # ──────────────── ADMIT SOME PATIENTS TO ROOMS ──────────────────────────
    room_assignments = [
        ("PAT0001", "ICU1"),
        ("PAT0003", "ICU2"),
        ("PAT0007", "ICU3"),
        ("PAT0002", "R201"),
        ("PAT0005", "R202"),
        ("PAT0008", "R101"),
        ("PAT0010", "R102"),
        ("PAT0013", "R203"),
        ("PAT0017", "ICU1"),   # won't fit — ICU1 taken, shows occupancy check
    ]
    for pid, rno in room_assignments:
        h.admit_patient_to_room(pid, rno)

    # ──────────────── ASSIGN DOCTORS ────────────────────────────────────────
    assignments = [
        ("DOC0001", "PAT0001"),
        ("DOC0001", "PAT0002"),
        ("DOC0002", "PAT0005"),
        ("DOC0003", "PAT0003"),
        ("DOC0003", "PAT0007"),
        ("DOC0004", "PAT0013"),
        ("DOC0005", "PAT0008"),
        ("DOC0007", "PAT0015"),
        ("DOC0008", "PAT0004"),
        ("DOC0011", "PAT0006"),
    ]
    for did, pid in assignments:
        h.assign_doctor_to_patient(did, pid)

    # ──────────────── MEDICAL RECORDS ───────────────────────────────────────
    patient_objs[0].add_medical_record("Acute MI", "Thrombolysis + Aspirin", "Dr. Ayesha Tariq")
    patient_objs[2].add_medical_record("Ischemic Stroke", "tPA, BP management", "Dr. Sara Malik")
    patient_objs[6].add_medical_record("Hip Fracture", "ORIF surgery planned", "Dr. Farhan Ahmed")
    patient_objs[9].add_medical_record("Migraine", "Sumatriptan, rest", "Dr. Sara Malik")
    patient_objs[12].add_medical_record("COPD Exacerbation", "Steroids, Bronchodilators", "Dr. Kamran Iqbal")

    # ──────────────── PRESCRIPTIONS ─────────────────────────────────────────
    patient_objs[0].add_prescription("Aspirin 75mg",      "Once daily",  "Dr. Ayesha Tariq", 30)
    patient_objs[0].add_prescription("Atorvastatin 40mg", "Once at night","Dr. Ayesha Tariq", 90)
    patient_objs[2].add_prescription("Clopidogrel 75mg",  "Once daily",  "Dr. Sara Malik",   60)
    patient_objs[9].add_prescription("Sumatriptan 50mg",  "As needed",   "Dr. Sara Malik",   14)

    # ──────────────── APPOINTMENTS ──────────────────────────────────────────
    appt_data = [
        ("PAT0004",  "DOC0001", "2026-05-05", "10:00", "Follow-up chest pain"),
        ("PAT0006",  "DOC0011", "2026-05-05", "11:00", "Prenatal checkup"),
        ("PAT0009",  "DOC0005", "2026-05-06", "09:30", "Knee pain"),
        ("PAT0011",  "DOC0002", "2026-05-06", "14:00", "ECG review"),
        ("PAT0014",  "DOC0004", "2026-05-07", "10:30", "Headache evaluation"),
        ("PAT0016",  "DOC0009", "2026-05-07", "15:00", "Skin rash"),
        ("PAT0018",  "DOC0008", "2026-05-08", "09:00", "Pre-op assessment"),
        ("PAT0020",  "DOC0010", "2026-05-08", "11:00", "Eye exam"),
        ("PAT0012",  "DOC0007", "2026-05-09", "14:30", "Vaccination"),
        ("PAT0019",  "DOC0012", "2026-05-09", "16:00", "Ear wax removal"),
    ]
    for pid, did, dt, tm, notes in appt_data:
        h.book_appointment(pid, did, dt, tm, notes)

    # ──────────────── QUEUES ────────────────────────────────────────────────
    queue_data = [
        ("PAT0001", "Cardiology"),
        ("PAT0005", "Cardiology"),
        ("PAT0011", "Cardiology"),
        ("PAT0003", "Neurology"),
        ("PAT0007", "Neurology"),
        ("PAT0014", "Neurology"),
        ("PAT0008", "Orthopedics"),
        ("PAT0009", "Orthopedics"),
        ("PAT0015", "Pediatrics"),
        ("PAT0012", "Pediatrics"),
        ("PAT0004", "General Surgery"),
        ("PAT0013", "General Surgery"),
        ("PAT0006", "Gynecology"),
        ("PAT0018", "Gynecology"),
        ("PAT0016", "Dermatology"),
        ("PAT0020", "Ophthalmology"),
        ("PAT0019", "ENT"),
    ]
    for pid, spec in queue_data:
        h.add_patient_to_queue(pid, spec)

    # ──────────────── BILLS ─────────────────────────────────────────────────
    bill_patients = [
        ("PAT0001", [
            ("Consultation Fee (Cardiology)", 3000, 1),
            ("ECG",                           1500, 1),
            ("Troponin Blood Test",           2500, 1),
            ("ICU Room (2 days)",            15000, 2),
            ("Thrombolysis Medication",      25000, 1),
        ], 0, True),
        ("PAT0002", [
            ("Consultation Fee",             2500, 1),
            ("Private Room (1 day)",         6000, 1),
            ("Blood Panel",                  1800, 1),
        ], 10, False),
        ("PAT0003", [
            ("Consultation Fee (Neurology)", 3500, 1),
            ("MRI Brain",                   12000, 1),
            ("ICU Room (3 days)",           15000, 3),
            ("tPA Medication",              40000, 1),
        ], 5, False),
        ("PAT0008", [
            ("Consultation Fee",             2800, 1),
            ("X-Ray Hip",                    2000, 1),
            ("General Room (1 day)",         2500, 1),
        ], 0, True),
        ("PAT0013", [
            ("Consultation Fee (Neurology)", 3200, 1),
            ("Private Room (4 days)",        6000, 4),
            ("CT Scan Chest",                8000, 1),
            ("Steroid Medication",           5000, 1),
            ("Bronchodilator Nebulisation",   800, 5),
        ], 15, False),
    ]
    for pid, items, disc, paid in bill_patients:
        b = h.create_bill(pid)
        if b:
            for desc, amt, qty in items:
                b.add_item(desc, amt, qty)
            b.discount_percent = disc
            if paid:
                b.pay()

    print("\n  ✓ Seed data loaded successfully.\n")
