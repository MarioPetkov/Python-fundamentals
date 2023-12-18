number = int(input())
plant_info = {}
for n in range(number):
    plant, rarity = input().split('<->')
    plant_info[plant] = rarity

while command != ""