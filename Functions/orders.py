def order(type, qty):
    if type == "coffee":
        result = qty * 1.50
    elif type == "water":
        result = qty * 1.00
    elif type == "coke":
        result = qty * 1.40
    elif type == "snacks":
        result = qty * 2.00
    return f'{result:.2f}'

type = input()
qty = int(input())
print(order(type, qty))