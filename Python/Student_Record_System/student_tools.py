def add_student(name, department, level):
    student = {
        "name": name,
        "department": department,
        "level": level
    }
    return student
def display_student(student):
    print("\nStudent Record")
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']}")
    print(f"Level: {student['level']}")
