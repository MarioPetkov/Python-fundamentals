def animals_info(animal_name, daily_food, area):
    if not areas[area] in areas.keys():
        areas[area] = 0
    else: 
        areas[area] += 1
    if not animal_name in animals.keys():
        animals[animal_name] = {"daily_food_qty": daily_food, "area": area}
        
        return animals[animal_name], areas[area]
    else:
        animals[animal_name]["daily_food_qty"] += daily_food
        animals[animal_name]["area"] += area
        
        return animals[animal_name]["daily_food_qty"], animals[animal_name]["area"], areas[area]

animals = {}
areas = {}
command = input().split(': ')
while command[0] != "EndDay":
    animal_info = command[1].split('-')
    if command[0] == "Add":
        animal_name, daily_food, area = animal_info[0], int(animal_info[1]), animal_info[2] 
        animals_info(animal_name, daily_food, area)
        

    command = input().split(': ')
print("Animals:")
for animal in animals:
    print(f" {animal} -> {animals[animal]['daily_food_qty']}g")
print("Areas with hungry animals:")
for area in areas:
    print(f" {area} -> {areas[area]}")

#Add: Adam-4500-ByTheCreek
#Add: Maya-7600-WaterfallArea
#Add: Maya-1230-WaterfallArea
#Feed: Jamie-2000
#EndDay