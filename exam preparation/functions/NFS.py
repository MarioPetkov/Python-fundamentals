
number_of_cars = int(input())
cars = {}
for car_themself in range(number_of_cars):
    car_characteristics = input().split('|')
    model, mileage, fuel_available = car_characteristics[0], int(car_characteristics[1]), int(car_characteristics[2])
    cars[model] = {"mileage": mileage, "fuel_available": fuel_available}
command = input().split(' : ')
while command[0] != "Stop":
    if command[0] == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car]["fuel_available"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel_available"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            cars.pop(car)
            print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car, fuel = command[1], int(command[2]) 
        max_fuel = 75
        refilled_fuel = min((cars[car]["fuel_available"] + fuel), max_fuel)
        print(f"{car} refueled with {refilled_fuel - cars[car]['fuel_available']} liters")
        cars[car]["fuel_available"] = refilled_fuel
    elif command[0] == "Revert":
        car, kilometers = command[1], int(command[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input().split(' : ')
    
for car, car_information in cars.items():
    print(f"{car} -> Mileage: {car_information['mileage']} kms, Fuel in the tank: {car_information['fuel_available']} lt.")