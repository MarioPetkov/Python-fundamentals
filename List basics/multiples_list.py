factor = int(input())
count = int(input())
list = []
for multiples in range(1, count + 1):
    list.append(factor * multiples)
print(list)