list_with_numbers = input().split()
opposite_number = []
for i in list_with_numbers:
    current_number = -int(i)
    opposite_number.append(current_number)
print(opposite_number)