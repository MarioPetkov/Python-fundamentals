import re

sequence = input()
pattern = r'(::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*)'
coolThreshholdPattern = r'\d'
coolThreshhold = re.findall(coolThreshholdPattern, sequence)
coolthreshholdsum = 1

for num in coolThreshhold:
    coolthreshholdsum *= int(num)

matched_words = re.findall(pattern, sequence)
cool_emojis = []

for match in matched_words:
    coolness = sum(ord(char) for char in match[2:-2])
    if coolness > coolthreshholdsum:
        cool_emojis.append((match))

print(f"Cool threshold: {coolthreshholdsum}")
print(f"{len(matched_words)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(f'{emoji}')
