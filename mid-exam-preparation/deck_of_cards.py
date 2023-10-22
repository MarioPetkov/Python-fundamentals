def add(list_of_cards: list, command: list):
    if command[1] in list_of_cards:
        print("Card is already in the deck")
    else:
        list_of_cards.append(command[1])
        print("Card successfully added")

def remove(list_of_cards: list, command: list):
    if command[1] not in list_of_cards:
        print("Card not found")
    else:
        list_of_cards.remove(command[1])
        print("Card successfully removed")

def remove_at(list_of_cards, command):
    current_index = int(command[1])
    if current_index not in range(len(list_of_cards)):
        print("Index out of range")
    else:
        list_of_cards.pop(current_index)
        print("Card successfully removed")  
def insert(list_of_cards, command):
    card_name = command[2]
    current_index = int(command[1])
    if current_index not in range(len(list_of_cards)):
        print("Index out of range")
    elif current_index in range(len(list_of_cards)) and card_name in list_of_cards:
        print("Card is already added")
    else: 
        list_of_cards.insert(current_index, card_name)
        print("Card successfully added")      
list_of_cards = input().split(", ")
number_of_commands = int(input())
for number in range(number_of_commands):
    command = input().split(", ")
    if command[0] == "Add":
        add(list_of_cards, command)
    elif command[0] == "Remove":
        remove(list_of_cards, command)
    elif command[0] == "Remove At":
        remove_at(list_of_cards, command)
    elif command[0] == "Insert":
        insert(list_of_cards, command)
result = ", ".join(list_of_cards)
print(result)