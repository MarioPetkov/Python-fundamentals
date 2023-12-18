spices = input().split(', ')
while True:
    command = input().split(' ')
    if command[0] == "done":
        break
    elif command[0] == "AddSpice":
        if not command[1] in spices:
            spices.append(command[1])
    elif command[0] == "AddManySpices":
        index = int(command[1])
        spices_list = command[2].split('|')
        spices[index:index] = spices_list
    elif command[0] == "SwapSpices":
        if command[1] in spices and command[2] in spices:
            index1 = spices.index(command[1])
            index2 = spices.index(command[2])
            spices[index1], spices[index2] = spices[index2], spices[index1]
    elif command[0] == "ThrowAwaySpices":
        if command[1] in spices:
            index = spices.index(command[1])
            add_index = int(command[2])
            spices = spices[:index] + spices[index + add_index:]
    elif command[0] == "Arrange":
        spices = sorted(spices)
print(' '.join(spices))