import re

strings_count = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[(\w{8,})]'
for word in range(strings_count):
    string = input()
    matched_word = re.findall(pattern, string)
    if matched_word:
            for match in matched_word:
                command = match[0] + ':'
                word = match[1]
                sequence = []
            for letter in word:
                sequence.append(ord(letter))
            print(command, *sequence, sep = ' ')
    else:
        print("The message is invalid")