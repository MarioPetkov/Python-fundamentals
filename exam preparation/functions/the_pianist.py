

data = {}


piece_number = int(input())
for _ in range(piece_number):
    piece, composer, key = input().split('|')
    data[piece] = {"Composer": composer, "Key": key}
    
command = input().split('|')
while True:
    if command[0] == "Stop":
        break
    if command[0] == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece in data.keys():
            print(f"{piece} is already in the collection!")
        else:
            data[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in data.keys():
            print(f"Successfully removed {piece}!")
            del data[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in data.keys():
            data[piece]["Key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input().split('|')


for pianist in data.keys():
    
    print(f"{pianist} -> Composer: {data[pianist]['Composer']}, Key: {data[pianist]['Key']}")
