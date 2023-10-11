def calculations(operator, a, b):
    if operator == "multiply":
        return a * b
    if operator == "divide":
        return int(a / b)
    if operator == "add":
        return a + b
    if operator == "distract":
        return a - b


input_operator = input()
first_num = int(input())
second_num = int(input())
print(calculations(input_operator, first_num, second_num))