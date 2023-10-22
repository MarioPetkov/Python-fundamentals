groceries = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)
    elif action == "Unnecessary":
        if item in groceries:
             groceries.remove(item) 
    elif action == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item
    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
print(", ".join(groceries))

