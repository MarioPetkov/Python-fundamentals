first_word = input()
second_word = input()
last_printed_word = first_word
for character_index in range(len(first_word)):
    left_part = second_word[:character_index + 1]
    right_part = first_word[character_index + 1:]
    new_string = left_part + right_part
    if new_string == last_printed_word:
        continue
    print(new_string)
    last_printed_word = new_string