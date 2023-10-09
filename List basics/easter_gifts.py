names_of_the_gifts = input().split()
while True:
    command = input()
    if command == "No Money":
        break
    else:
        command = command.split()
        if "OutOfStock" in command:
            item = command[1]
            for element in names_of_the_gifts:
                if element == item:
                    index_to_replace = names_of_the_gifts.index(element)
                    names_of_the_gifts[index_to_replace] = "None"
        elif "Required" in command:
            item = command[1]
            index_to_replace = int(command[2])
            if index_to_replace < len(names_of_the_gifts):
                names_of_the_gifts[index_to_replace] = command[1]
        elif "JustInCase" in command:
            item = command[1]
            names_of_the_gifts[-1] = item
for item in names_of_the_gifts:
    if item != "None":
        print(item, end = " ")
