first_index = int(input())
last_indes = int(input())
for character in range(first_index, last_indes + 1):
    char_str = chr(character)
    print(char_str, end = " ")