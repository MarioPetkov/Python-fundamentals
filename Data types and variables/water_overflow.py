water_tank_capacity_liters = 255
poured_water = 0
num_of_lines = int(input())
for n in range(num_of_lines):
    liters = int(input())
    poured_water += liters
    if water_tank_capacity_liters < poured_water:
        print("Insufficient capacity!")
        poured_water -= liters
        continue
print(poured_water)