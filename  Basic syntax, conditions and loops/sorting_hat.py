student_name = input()
while True:
    if student_name == "Welcome!":
        print(f"Welcome to Hogwarts.")
        break
    if student_name == "Voldemort":
        print("You must not speak of that name!")
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
    