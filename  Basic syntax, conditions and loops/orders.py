num_of_orders = int(input())
total_price = 0
for i in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_for_day = int(input())
    price_for_coffee = price_per_capsule * days * capsules_for_day
    if price_for_coffee != 0:
        print(f"The price for the coffee is: ${price_for_coffee:.2f}")
    total_price += price_for_coffee
print(f"Total: ${total_price:.2f}")