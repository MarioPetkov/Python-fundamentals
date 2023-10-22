def main(travel_route: int, fuel: int, ammunition: int) -> str:
    for route in travel_route:
        if route == "Titan":
            print("You have reached Titan, all passengers are safe.")
            exit()
        command, number = route.split(" ")
        number = int(number)
        if command == "Travel":
            fuel = travel(fuel, number)
        elif command == "Enemy":
            fuel, ammunition = enemy(fuel, ammunition, number)
        elif command == "Repair":
            fuel, ammunition = repair(fuel, ammunition, number)
    return fuel, ammunition

def travel(fuel:int, number:int) -> int:
    fuel -= number
    if fuel >= 0:
        print(f"The spaceship travelled {number} light-years.")
    else:
        print("Mission failed")
        exit()
    return fuel

def enemy(fuel:int, ammunition:int, number:int) -> int:
    if ammunition >= number:
        ammunition -= number
        print(f"An enemy with {number} armour is defeated.")
    elif fuel >= number * 2:
        fuel -= number * 2
        print(f"An enemy with {number} armour is outmaneuvered.")
    else:
        print("Mission failed.")
        exit()
    return fuel, ammunition

def repair(fuel:int, ammunition:int, number:int) -> int:
    ammunition += number * 2
    fuel += number
    print(f"Ammunitions added: {number * 2}.")
    print(f"Fuel added: {number}.")
    return ammunition, fuel

travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())
main(travel_route, fuel, ammunition)

    