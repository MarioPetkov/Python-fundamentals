student_name = input()
while student_name != "Welcome!":
    if student_name == "Voldemort":
        print("You must not speak off that name!")
        break
    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    if len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    if len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    if len(student_name) > 6:
        print(f"{student_name} goes to Hufflepuff.")
    student_name = input()
print(f"Welcome to Hogwarts.")