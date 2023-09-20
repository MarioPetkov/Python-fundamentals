inputs = int(input())
for i in range(inputs):
    strings = str(input())
    if "_" in strings or "," in strings or "." in strings:
        print(f"{strings} is not pure!")
    else:
        print(f"{strings} is pure.")