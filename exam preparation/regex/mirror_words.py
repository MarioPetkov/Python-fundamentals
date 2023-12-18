import re

text = input()
pattern = r'([#@])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
matched_words = re.findall(pattern, text)
mirror_words = []
result = len(matched_words)
if not matched_words:
    print("No word pairs found!")
else:
    print(f'{result} word pairs found!')
for match in matched_words:
    first_word, second_word = match[1], match[2]
    if first_word == second_word[::-1]:
        mirror_words.append(f'{first_word} <=> {second_word}')
if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")