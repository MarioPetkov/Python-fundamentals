budget = float(input())
flavour_kg = float(input())
eggs_pack = flavour_kg * 0.75
milk_litre = flavour_kg * 1.25
bread_price = flavour_kg + eggs_pack + milk_litre * 0.25
remaining_budget = budget
colored_eggs = 0
bread = 0
while remaining_budget > bread_price:
    remaining_budget -= bread_price
    bread += 1
    colored_eggs += 3
    if bread % 3 == 0:
        colored_eggs -= 2

print(f"You made {bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left")

#recipe
#eggs 1 pack
#flour 1 kg
#milk 0.25ml