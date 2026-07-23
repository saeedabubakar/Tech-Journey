import student_tools
number = int(input("How many students do you want to enter? "))
students = []
for i in range(number):
    name = input("Enter student name: ")
    department = input("Enter department: ")
    try:
        level = int(input("Enter level: "))
    except ValueError:
        print(f"Level must be a number.")
        exit()
    student = student_tools.add_student(
        name,
        department,
        level)
    students.append(student)
for student in students:
    student_tools.display_student(student)
with open("student.txt", "a") as file:
    for student in students:
        file.write(
            f"{student['name']}, "
            f"{student['department']}, " 
            f"{student['level']}\n"
            )

