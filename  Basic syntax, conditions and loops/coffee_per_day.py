activity = input()
coffees = 0
while True:
    if activity == "END":
        print(coffees)
        break
    if activity == "coding" or activity == "dog" or activity == "cat" or activity == "movie":
        coffees += 1
    if activity == "CODING" or activity == "DOG" or activity == "CAT" or activity == "MOVIE":
        coffees += 2
    if coffees > 5:
        print("You need extra sleep")
        break
    activity = input()