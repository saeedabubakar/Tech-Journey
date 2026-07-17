try:
    name = input("Enter student name: ")
    score = int(input("Enter score: ")) 
    print(f"Student: {name}")
    print(f"Score: {score}")
except ValueError:
    print(f"Score must be a number.")
    