import re

inputs_num = int(input())
pattern = re.compile(r'([*@])([A-Z][a-z]{2,})\1:\s\[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|$')

for _ in range(inputs_num):
    message = input()
    matches = pattern.findall(message)
    
    if matches:
        for match in matches:
            tag_char = match[0]
            tag = match[1]
            group1 = match[2]
            group2 = match[3]
            group3 = match[4]

            if (group1 != group2) and (group2 != group3) and (group1 != group3):
                print(f'{tag}: {ord(group1)} {ord(group2)} {ord(group3)}')
    else:
        print("Valid message not found!")
