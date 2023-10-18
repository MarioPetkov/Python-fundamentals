def is_even(number):
    if number % 2 == 0:
        return True
    return False

numbers_as_string = input().split()
numbers_as_digit = []
for number in numbers_as_string:
    numbers_as_digit.append(int(number)) 
result = list(filter(is_even, numbers_as_digit))
print(result)