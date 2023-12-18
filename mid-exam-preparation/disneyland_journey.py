
journey_price = float(input())
months = int(input())
money = 0
for month in range(1, months + 1):
    if month > 1 and month % 2 == 1:
        money -= money * 0.16
    if month % 4 == 0:
        money += money * 0.25
    money += 0.25 * journey_price
if money >= journey_price:
    print(f"Bravo! You can go to Disneyland and you will have {money-journey_price:.2f}lv. for souvenirs.")
else: 
    print(f"Sorry. You need {journey_price - money:.2f}lv. more.")