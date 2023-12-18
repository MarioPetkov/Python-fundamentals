
command = input().split(':')
animals = {}
areas = {}

while command[0] != "EndDay":
    animal_information = command[1].split('-')
    if command[0] == "Add":
        animal_name, daily_food_qty, area = animal_information[0], int(animal_information[1]), animal_information[2]
        if not animal_name in animals:
            animals[animal_name] = {"daily_food_qty": daily_food_qty, "area": area}
            
        else:
            animals[animal_name]["daily_food_qty"] += daily_food_qty

    if command[0] == "Feed":
        animal_name, food = animal_information[0], int(animal_information[1])
        if animal_name in animals:
            animals[animal_name]["daily_food_qty"] -= food
            if animals[animal_name]["daily_food_qty"] <= 0:
                animals.pop(animal_name)

                print(f"{animal_name} was successfully fed")
            else:
               hungry_area[area]["hungry_animals"] += 1
            

    
    command = input().split(':')
print("Animals:")
for animal in animals:
    print(f" {animal} -> {animals[animal]['daily_food_qty']}g")
for area in areas:
    print(f" {area} -> {areas[area]}")
print("Areas with hungry animals:")

#for area, animal_in_area in areas.items():
    #hungry_animals = sum(1 for animal in animals_in_area) 
#    if animals[animal] > 0:
 #       if hungry_animals > 0:
  #          print(f" {area}: {hungry_animals})

