first_character = input()
second_character = input()
random_string = input()
total_value = 0
for character in random_string:
    if ord(first_character) < ord(character) < ord(second_character):
        total_value += ord(character)
print(total_value)