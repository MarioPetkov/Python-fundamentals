num = int(input())
result = False
if num % 2 == 0 and num % 3 == 0:
    result = True
if result == True:
    print(result)
num = int(input("Enter an integer: "))

if result == True:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")