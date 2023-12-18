num_strings = int(input())
name_begin, name_end = "@", "|"
age_begin, age_end = "#", "*"
name = ""
age = ""
for string in range(num_strings):
    person_string = input()
    name_begin_index, name_end_index = person_string.index(name_begin), person_string.index(name_end)
    age_begin_index, age_end_index = person_string.index(age_begin), person_string.index(age_end)
    for index in range(name_begin_index + 1, name_end_index):
        name = name + person_string[index]
    for index in range(age_begin_index + 1, age_end_index):
        age = age + person_string[index]
    print(f"{name} is {age} years old.")
    name = ""
    age = ""
    