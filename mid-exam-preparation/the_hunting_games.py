days_of_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())
water_per_person_for_one_day = float(input())
food_per_person_for_one_day = float(input())
total_water = days_of_adventure * count_of_players * water_per_person_for_one_day
total_food = days_of_adventure * count_of_players * food_per_person_for_one_day

for day in range(1, days_of_adventure+1):
    current_energy = float(input())
    group_energy -= current_energy
    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break
    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        group_energy *= 1.1
        total_food -= total_food / count_of_players
    if day == days_of_adventure:
        break

if group_energy > 0: print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
