num_of_integers = int(input())
numbers = []
filtered_list = []
for num in range(num_of_integers):
    current_number = int(input())
    numbers.append(current_number)
command = input()
if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered_list.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered_list.append(num)
if command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_list.append(num)
elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered_list.append(num)
print(filtered_list)