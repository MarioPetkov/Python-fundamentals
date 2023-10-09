num_of_characters = int(input())
total_sum = 0 
for character in range(num_of_characters):
    current_character = input()
    char_num = ord(current_character)
    total_sum += char_num
print(f"The sum equals: {total_sum}")