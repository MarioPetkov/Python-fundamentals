divisor = int(input())
boundary = int(input())

while boundary % divisor != 0:
    boundary -= 1
print(boundary)