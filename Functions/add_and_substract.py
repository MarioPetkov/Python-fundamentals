def sum_numbers(a, b):
    return a + b
def subtract(result, c):
    return result - c
def add_and_subtract(a, b, c):
    returned_result = sum_numbers(first_number, second_number)
    final_result = subtract(returned_result, third_number)
    return final_result
first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
