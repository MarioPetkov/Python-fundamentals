import re

text_string = input()
normal_day_calories = 2000
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
food_list = re.findall(pattern, text_string)
total_calories = sum([int(match[5]) for match in food_list])
days = total_calories // normal_day_calories
print(f"You have food to last you for: {days} days!")
for element in food_list:
    item_name, expiration_date, calories = element[1], element[3], element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")



