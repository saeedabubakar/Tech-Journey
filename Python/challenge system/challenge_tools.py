def add_student(name, department, level):
    student = {
        "name": name,
        "department": department,
        "level": level
    }
    return student
def display_student():
    with open ("student.txt" "r") as file:
        for line in file:
            print(line)
        
    