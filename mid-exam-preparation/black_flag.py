days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
gained_plunder = 0

for day in range(1, days_of_plunder+1):
    gained_plunder += daily_plunder
    if int(day) % 3 == 0:
        gained_plunder += daily_plunder * 0.5
    if int(day) % 5 == 0:
        gained_plunder -= gained_plunder * 0.3



if gained_plunder >= expected_plunder:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
else:
    percentage = 100 * (gained_plunder / expected_plunder)
    print(f"Collected only {percentage:.2f}% of the plunder.")