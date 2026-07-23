print("Student Record System")
print("1. Add Student")
print("2. Show Students")
print("3. Exit")
try:
    choice = int(input("Choose an option: "))
except ValueError:
    print("choice must be a number")
    exit()
import challenge_tools
students = []
if choice == 1:
    name = input("Enter student name: ")
    department = input("Enter department: ")
    level = int(input("Enter level: "))
    student = challenge_tools.add_student(
    name,
    department,
    level
    )
    students.append(student)
    with open("student.txt", "a") as file:
        file.write(
            f"{student['name']}, "
            f"{student['department']}, "
            f"{student['level']}\n"
        )
elif choice == 2:
    with open ("student.txt", "r") as file:
        for line in file:
            print(line)
elif choice == 3:
    print("Goodbye engineer!")
else:
    print("Invalid choice.")
