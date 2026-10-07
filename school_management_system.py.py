print("══════════════════════════════════════════════════════════")
print("              WELCOME TO CLASS MANAGEMENT SYSTEM")
print("          (Mr, Hany Hassan Mohammed) : CREATED BY")
print("                     LOGIN | 1/4")
print("               CLASS MANAGEMENT SYSTEM | 1/4")
print("══════════════════════════════════════════════════════════")

while True:
    teacher_name = input("                    Mr, ").strip()

    if teacher_name:
        break

    print("              Please enter your name to continue.")

print()
print("══════════════════════════════════════════════════════════")
print("                  WELCOME TO MY PROGRAM")
print(f"                     Mr,{teacher_name}")
print("                       Class 1/4")
print("                 Login completed successfully ✓")
print("══════════════════════════════════════════════════════════")

input("\n          Press Enter to continue to the main menu...")

students = [
    {"name": "Omar Salah Abdel Aziz", "status": "Regular", "attendance": "Excellent", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Amr El-Sayed Abdel Hamid", "status": "Regular", "attendance": "Good", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Fares Ibrahim El-Shahat Ibrahim", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Fares El-Sayed El-Sayed Metwally", "status": "Regular", "attendance": "Acceptable", "behavior": "Good", "activity": "Unknown", "level": "Acceptable", "role": ""},
    {"name": "Mohamed Ibrahim Saad", "status": "Regular", "attendance": "Excellent", "behavior": "Very Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Ahmed Abdel Rahman", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Ahmed Mostafa Gad", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed El-Sayed Abdel Gawad", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed El-Sayed Mohamed El-Sayed", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Tharwat Maher", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Khaled Ali Abdel Kader", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Rady Mahmoud", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Ragab Mohamed", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Saleh Ayesh", "status": "Regular", "attendance": "Excellent", "behavior": "Good", "activity": "Assistant Class Representative", "level": "", "role": "Assistant Class Representative"},
    {"name": "Mohamed Salah Abdel Latif", "status": "Regular", "attendance": "Good", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Salah Mohamed El-Sebaei", "status": "Regular", "attendance": "Very Good", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Abdel Hamid Mohamed Ahmed", "status": "Regular", "attendance": "Excellent", "behavior": "Very Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Abdel Latif El-Sayed Saber", "status": "Regular", "attendance": "Very Good", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Abdel Latif Mohamed", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mohamed Ali Ibrahim Suleiman", "status": "Regular", "attendance": "Excellent", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mahmoud Mohamed Rady", "status": "Regular", "attendance": "Good", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Marwan El-Sayed Salem", "status": "Regular", "attendance": "Good", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Mansour Mohamed Abdel Hamid", "status": "Regular", "attendance": "Good", "behavior": "Very Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Momen El-Sayed Mahmoud Metwally", "status": "Regular", "attendance": "Acceptable", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Hady Ahmed Askar", "status": "Regular", "attendance": "Excellent", "behavior": "Very Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Hany Hassan Mohammed Hassan Abu Shuaisha", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Scientific", "level": "", "role": ""},
    {"name": "Waseem Saleh Abdel Hamid", "status": "Regular", "attendance": "Good", "behavior": "Good", "activity": "Sports", "level": "", "role": ""},
    {"name": "Walid Hussein Mohamed Desouky", "status": "Regular", "attendance": "Excellent", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Yazid Mansour El-Shenawy", "status": "Regular", "attendance": "Very Good", "behavior": "Excellent", "activity": "Class Leader", "level": "", "role": "Class Leader"},
    {"name": "Youssef Abdel Mohsen Adel", "status": "Regular", "attendance": "Good", "behavior": "Excellent", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Youssef Mohamed Abdel Razek", "status": "Regular", "attendance": "Good", "behavior": "Good", "activity": "Unknown", "level": "", "role": ""},
    {"name": "Salah Mohamed Abbas", "status": "Repeating Year", "attendance": "Good", "behavior": "Acceptable", "activity": "Unknown", "level": "", "role": ""}
]


def derive_level_from_behavior(behavior):
    behavior = behavior.strip()

    if behavior == "Excellent":
        return "Excellent"

    if behavior in ("Very Good", "VeryGood"):
        return "Very Good"

    if behavior == "Good":
        return "Good"

    if behavior == "Acceptable":
        return "Acceptable"

    return "Unknown"


for student in students:
    if not student.get("activity"):
        student["activity"] = "Unknown"

    if not student.get("level"):
        student["level"] = derive_level_from_behavior(student.get("behavior", ""))


def main_menu():
    print()
    print("══════════════════════════════════════════════════════════")
    print("                         MAIN MENU")
    print("                       CLASS 1/4")
    print("══════════════════════════════════════════════════════════")
    print("1 - Show Student List")
    print("2 - Show Student Data by Number")
    print("3 - Search Student by Name")
    print("4 - Class Statistics")
    print("5 - Show Hany's Profile")
    print("6 - Show Class Leader and Assistant")
    print("0 - Exit")
    print("══════════════════════════════════════════════════════════")


def return_to_menu():
    print()
    print("──────────────────────────────────────────────────────────")
    input("Press Enter to return to the main menu...")
    print("──────────────────────────────────────────────────────────")


def show_student_list():
    print()
    print("══════════════════════════════════════════════════════════")
    print("                       STUDENT LIST")
    print("                         CLASS 1/4")
    print("══════════════════════════════════════════════════════════")

    for number, student in enumerate(students, start=1):
        role = f" ({student['role']})" if student["role"] else ""
        print(f"{number:02} │ {student['name']}{role}")

    print("══════════════════════════════════════════════════════════")


def show_student_profile(student_number):
    student = students[student_number - 1]

    print()
    print("══════════════════════════════════════════════════════════")
    print("                     STUDENT PROFILE")
    print("                     COMPLETE DATA")
    print("══════════════════════════════════════════════════════════")
    print(f"Name                : {student['name']}")
    print("Class               : 1/4")
    print(f"Status              : {student['status']}")
    print(f"Attendance          : {student['attendance']}")
    print(f"Behavior            : {student['behavior']}")
    print(f"Activity            : {student['activity']}")
    print(f"Academic Level      : {student['level']}")

    if student["role"]:
        print(f"Role                : {student['role']}")

    print("Notes               : No notes available")
    print("══════════════════════════════════════════════════════════")


def choose_student():
    show_student_list()

    student_number_text = input("\nEnter student number (0 to return): ").strip()

    if not student_number_text.isdigit():
        print("Please enter a valid number.")
        return

    student_number = int(student_number_text)

    if student_number == 0:
        return

    if 1 <= student_number <= len(students):
        show_student_profile(student_number)
    else:
        print("Student number does not exist in this class.")


def search_students():
    print()
    print("══════════════════════════════════════════════════════════")
    print("                      STUDENT SEARCH")
    print("                 SEARCH BY NAME OR PART")
    print("══════════════════════════════════════════════════════════")

    search_name = input("Enter a name or part of a name: ").strip().casefold()

    if not search_name:
        print("Please enter a name or part of a name.")
        print("══════════════════════════════════════════════════════════")
        return

    found_students = []

    for number, student in enumerate(students, start=1):
        if search_name in student["name"].casefold():
            found_students.append((number, student))

    print()

    if found_students:
        print("Matching students:")
        print()

        for number, student in found_students:
            role = f" ({student['role']})" if student["role"] else ""
            print(f"{number:02} │ {student['name']}{role}")
    else:
        print("No student matched your search.")

    print("══════════════════════════════════════════════════════════")


def class_statistics():
    total_students = len(students)
    regular_students = sum(1 for student in students if student["status"] == "Regular")
    repeating_students = sum(1 for student in students if student["status"] == "Repeating Year")
    leader_count = sum(1 for student in students if student["role"] == "Class Leader")
    assistant_count = sum(1 for student in students if student["role"] == "Assistant Class Representative")

    print()
    print("══════════════════════════════════════════════════════════")
    print("                       CLASS INFO")
    print("                   CLASS STATISTICS")
    print("══════════════════════════════════════════════════════════")
    print("Class               : 1/4")
    print(f"Total students      : {total_students}")
    print(f"Regular students    : {regular_students}")
    print(f"Repeating students  : {repeating_students}")
    print(f"Class leader        : {leader_count}")
    print(f"Assistant           : {assistant_count}")
    print("System status       : ONLINE")
    print("Project language    : Python")
    print("System type         : Student Management System")
    print("Created by          : Hany Hassan Mohammed Hassan Abu Shuaisha")
    print("══════════════════════════════════════════════════════════")


def show_hany_profile():
    hany = next(
        student for student in students
        if student["name"] == "Hany Hassan Mohammed Hassan Abu Shuaisha"
    )

    print()
    print("══════════════════════════════════════════════════════════")
    print("                       HANY PROFILE")
    print("                   CREATOR INFORMATION")
    print("══════════════════════════════════════════════════════════")
    print(f"Name                : {hany['name']}")
    print("English Name        : Hany Hassan Mohammed")
    print("Class               : 1/4")
    print(f"Status              : {hany['status']}")
    print(f"Attendance          : {hany['attendance']}")
    print(f"Behavior            : {hany['behavior']}")
    print(f"Activity            : {hany['activity']}")
    print(f"Academic Level      : {hany['level']}")
    print("Favorite Subject    : Computer and Microsoft Word")
    print("Project Type        : Python")
    print("══════════════════════════════════════════════════════════")


def leadership_menu():
    leader = next(student for student in students if student["role"] == "Class Leader")
    assistant = next(student for student in students if student["role"] == "Assistant Class Representative")

    leader_number = students.index(leader) + 1
    assistant_number = students.index(assistant) + 1

    print()
    print("══════════════════════════════════════════════════════════")
    print("                    CLASS LEADERS")
    print("                   CLASS LEADERSHIP")
    print("══════════════════════════════════════════════════════════")
    print(f"1 - {leader['name']} (Class Leader) - Number: {leader_number}")
    print(f"2 - {assistant['name']} (Assistant Class Representative) - Number: {assistant_number}")
    print("══════════════════════════════════════════════════════════")

    leader_choice = input(
        "Choose 1 for Class Leader or 2 for Assistant (Enter to return): "
    ).strip()

    if leader_choice == "1":
        show_student_profile(leader_number)
    elif leader_choice == "2":
        show_student_profile(assistant_number)


while True:

    main_menu()

    choice = input("\nChoose an operation: ").strip()

    if choice == "1":
        show_student_list()
        return_to_menu()

    elif choice == "2":
        choose_student()
        return_to_menu()

    elif choice == "3":
        search_students()
        return_to_menu()

    elif choice == "4":
        class_statistics()
        return_to_menu()

    elif choice == "5":
        show_hany_profile()
        return_to_menu()

    elif choice == "6":
        leadership_menu()
        return_to_menu()

    elif choice == "0":
        print()
        print("══════════════════════════════════════════════════════════")
        print("                    SYSTEM CLOSED")
        print(f"                 THANK YOU, MR. {teacher_name}")
        print("                 FOR USING MY PROGRAM")
        print("                  HANY HASSAN MOHAMMED")
        print("                        CLASS 1/4")
        print("                   SESSION TERMINATED")
        print("══════════════════════════════════════════════════════════")
        break

    else:
        print()
        print("══════════════════════════════════════════════════════════")
        print("                     INVALID CHOICE")
        print("                Please choose a valid option.")
        print("══════════════════════════════════════════════════════════")
        return_to_menu()
