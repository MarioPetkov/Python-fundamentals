ticket_price = 150
items = input().split("|")
budget = float(input())
profit = 0
sold_items = 0
for item in range(len(items)):
    my_list = items[item].split("->")
    type = my_list[0]
    price = float(my_list[1])
    valid_price = False
    if type == "Clothes" and budget >= price <= 50:
        valid_price = True
    elif type == "Shoes" and budget >= price <= 35:
        valid_price = True
    elif type == "Accessories" and budget >= price <= 20.5:
        valid_price = True
    if valid_price:
        budget -= price
        sold_item = price * 1.4
        print(f"{sold_item:.2f}", end = " ")
        sold_items += sold_item
        profit += sold_item - price
budget += sold_items
print()
print(f"Profit: {profit:.2f}")        
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")

        