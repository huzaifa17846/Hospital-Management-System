**PROJECT DESCRIPTION**

City General Hospital --- Management System

Version 1.0 \| May 2026

**1. Project Overview**

The City General Hospital Management System is a comprehensive, dual-layer software solution designed to streamline and digitise the day-to-day operations of a modern hospital. It consists of two complementary components: a fully interactive command-line backend built in Python and a polished, browser-based graphical front-end built in HTML, CSS, and JavaScript.

Together, these components allow hospital administrators, receptionists, and clinical staff to manage patients, doctors, rooms, billing, appointments, queues, and non-clinical personnel from a single unified platform --- with no external database or server required.

**2. System Components**

**2.1 Python Backend (CLI Application)**

The backend is a pure Python application organised using object-oriented principles. It is run from the terminal via main.py and provides a fully interactive menu-driven interface for complete hospital management.

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| **Component**    | **Details**                                                                  |
| **Entry Point**  | main.py --- Interactive CLI with nested menus and input validation           |
| **Core Engine**  | hospital.py --- Central registry and business logic hub                      |
| **Data Model**   | person.py --- Abstract base; patient.py, doctor.py, staff.py inherit from it |
| **Supporting**   | room.py, appointment.py, bill.py, specialization.py                          |
| **Seed Data**    | data_seeder.py --- Pre-populates the system with realistic sample records    |
| **Language**     | Python 3.10+ (uses union type hints and dataclasses)                         |
| **Dependencies** | Standard library only --- no external packages required                      |

**2.2 Web Front-End (Browser UI)**

The front-end is a single self-contained HTML file (HospitalSystem_UI.html) that runs entirely in the browser. It mirrors all modules of the Python backend in a visually polished dark-mode dashboard.

|                   |                                                                           |
|-------------------|---------------------------------------------------------------------------|
| **Component**     | **Details**                                                               |
| **Technology**    | Vanilla HTML5, CSS3, JavaScript (ES6+) --- no frameworks or build tools   |
| **Fonts**         | Playfair Display (headings), DM Sans (body), DM Mono (data/figures)       |
| **Theme**         | Dark navy palette with blue accent glows and colour-coded status badges   |
| **State**         | In-memory JavaScript object --- resets on page refresh (no server needed) |
| **Seed Data**     | seedData() pre-loads sample patients, doctors, rooms, and staff on load   |
| **Currency**      | All monetary values displayed in Pakistani Rupees (Rs.)                   |
| **Compatibility** | Works in any modern browser --- Chrome, Firefox, Edge, Safari             |

**3. Functional Modules**

Both the CLI and the UI implement the same eight core modules:

|                  |                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Module**       | **Key Features**                                                                                                                                                                                |
| **Dashboard**    | Live stat cards for total patients, doctors, occupied rooms, and revenue. Summary widgets for recent activity across all modules.                                                               |
| **Patients**     | Register patients with full demographics, blood group, allergies, and urgency status (Normal / Urgent / Super-Urgent). View profiles, medical history, and prescriptions. Search by name or ID. |
| **Doctors**      | Add and manage doctors with specialization, qualification, years of experience, and consultation fees. Track availability status and assigned patient lists.                                    |
| **Rooms**        | View room availability in a visual grid. Allot rooms to patients, move patients between rooms, and vacate rooms on discharge.                                                                   |
| **OPD Queue**    | Manage the outpatient department waiting queue. Add patients to the queue, call the next patient, and track queue depth in real time.                                                           |
| **Appointments** | Book and track appointments between patients and doctors with date/time and status (Scheduled / Completed / Cancelled).                                                                         |
| **Billing**      | Generate itemised bills per patient, add line items with quantity and unit cost, apply percentage discounts, and mark bills as Paid or Unpaid.                                                  |
| **Staff**        | Register non-clinical staff (nurses, receptionists, lab technicians, etc.) with role, department, shift, and salary. View and filter the staff roster.                                          |

**4. Object-Oriented Design (Backend)**

The Python backend follows a clean class hierarchy with encapsulation and inheritance:

- Person (base class) --- shared attributes: ID, name, age, gender, phone

- Patient extends Person --- adds blood group, allergies, medical history, prescriptions, room assignment

- Doctor extends Person --- adds specialization, qualification, availability, patient list, appointments

- Staff extends Person --- adds role, department, salary, shift

- Hospital --- owns all entity registries and all business logic methods

- Room, Appointment, Bill, Specialization --- independent supporting entities

All entity IDs are auto-incremented and prefixed (PAT0001, DOC0001, STF0001, etc.) to prevent collisions. Sensitive attributes are private with controlled access through Python properties.

**5. Key Features & Highlights**

**Dual Interface**

The system provides identical functionality through both a terminal CLI and a graphical browser UI, giving developers and end-users flexibility in how they interact with the data.

**Zero External Dependencies**

The Python backend uses the Python standard library only. The HTML front-end is a single file with no npm packages, frameworks, or backend server required. Both can be run instantly without any installation steps beyond Python itself.

**Data Seeding**

Both layers ship with realistic pre-loaded data (patients, doctors, staff, rooms, bills) so the system is immediately demonstrable without any manual data entry.

**Input Validation**

The CLI enforces strict type and range checking on all inputs (age 0-130, valid blood groups, valid status codes, etc.) with informative error messages. The UI mirrors this with toast notifications for error and success feedback.

**Global Search**

The browser UI includes a top-bar global search that instantly locates a patient or doctor by name or ID and navigates to their detail view.

**6. Intended Use Cases**

- Academic project demonstrating OOP principles (inheritance, encapsulation, polymorphism)

- Hospital administration prototype or proof-of-concept demo

- Front-end portfolio piece showcasing dark-mode dashboard design

- Training tool for hospital staff to learn management system workflows

- Base for extension into a full-stack application with a real database (e.g., SQLite, PostgreSQL)

**7. Current Limitations**

- No persistent storage --- data is lost when the Python process exits or the browser tab is closed

- No user authentication or role-based access control

- No real-time synchronisation between the Python backend and the HTML front-end (they are independent)

- Currency is hardcoded to Pakistani Rupees; no multi-currency support

- No export functionality (e.g., PDF reports, CSV export) in the current version

**8. File Structure**

|                            |                                                                 |
|----------------------------|-----------------------------------------------------------------|
| **Component**              | **Details**                                                     |
| **main.py**                | CLI entry point --- all menus and user interaction logic        |
| **hospital.py**            | Hospital class --- central business logic and entity registries |
| **person.py**              | Abstract Person base class                                      |
| **patient.py**             | Patient entity (extends Person)                                 |
| **doctor.py**              | Doctor entity (extends Person)                                  |
| **staff.py**               | Staff entity (extends Person)                                   |
| **room.py**                | Room entity --- availability and patient assignment             |
| **appointment.py**         | Appointment entity --- booking and status tracking              |
| **bill.py**                | Bill entity --- itemised billing with discount support          |
| **specialization.py**      | Specialization/department registry                              |
| **data_seeder.py**         | Seeds the Hospital instance with realistic sample data          |
| **HospitalSystem_UI.html** | Complete browser-based front-end (single file)                  |

*End of Document*
