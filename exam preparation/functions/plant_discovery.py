number = int(input())
plants = {}

# Input processing
for n in range(number):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = {"rarity": 0, "rating": 0, 'count': 0}
    plants[plant]["rarity"] += rarity

# Command processing
while True:
    command = input()

    if command == 'Exhibition':
        break

    action, plant_data = command.split(': ')
    plant_data = plant_data.split(' - ')

    plant = plant_data[0]
    if plant in plants:
        if action == 'Rate':
            rating = int(plant_data[1])
            plants[plant]['rating'] += rating
            plants[plant]['count'] += 1
        elif action == 'Update':
            new_rarity = int(plant_data[1])
            plants[plant]['rarity'] = new_rarity
        elif action == 'Reset':
            plants[plant]['rating'] = 0
            plants[plant]['count'] = 0
    else:
        print("error")

# Output
print("Plants for the exhibition:")
for plant in plants:
    average_rating = plants[plant]['rating'] / plants[plant]['count'] if plants[plant]['count'] > 0 else 0
    print(f'- {plant}; Rarity: {plants[plant]["rarity"]}; Rating: {average_rating:.2f}')
