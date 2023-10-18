def calculations(operator, a, b):
    if operator == "multiply":
        result = a * b
    if operator == "divide":
        result = int(a / b)
    if operator == "add":
        result = a + b
    if operator == "subtract":
        result = a - b
    return result


input_operator = input()
first_num = int(input())
second_num = int(input())
print(calculations(input_operator, first_num, second_num))