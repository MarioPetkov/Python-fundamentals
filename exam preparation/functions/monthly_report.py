distributors = {}
clients = {}
total_income = 0

while True:
    command = input().split(' ')

    if command[0] == "End":
        break
    elif command[0] == "Deliver":
        distributor_name, money_spent = command[1], float(command[2])
        if distributor_name not in distributors:
            distributors[distributor_name] = money_spent
        else:
            distributors[distributor_name] += money_spent
    elif command[0] == "Return":
        distributor_name, money_returned = command[1], float(command[2])
        if distributor_name in distributors:
            if distributors[distributor_name] >= money_returned:
                distributors[distributor_name] -= money_returned
                if distributors[distributor_name] <= 0:
                    del distributors[distributor_name]
    elif command[0] == "Sell":
        client_name, money_earned = command[1], float(command[2])
        if client_name not in clients:
            clients[client_name] = money_earned
        else:
            clients[client_name] += money_earned
        total_income += money_earned

for client, money_earned in clients.items():
    print(f"{client}: {money_earned:.2f}")

print("-----------")

for distributor, money_spent in distributors.items():
    print(f"{distributor}: {money_spent:.2f}")

print("-----------")

print(f'Total Income: {total_income:.2f}')
