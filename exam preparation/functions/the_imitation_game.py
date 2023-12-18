def move(encrypted_message, number_of_letters):
    return encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

def insert(encrypted_message, index, value):
    return encrypted_message[:index] + value + encrypted_message[index:]

def change_all(encrypted_message, substring, replacement):
    return encrypted_message.replace(substring, replacement)

def decode_message(encrypted_message):
    while True:
        command = input().split('|')
        if command[0] == "Decode":
            break
        elif command[0] == "Move":
            number_of_letters = int(command[1])
            encrypted_message = move(encrypted_message, number_of_letters)
        elif command[0] == "Insert":
            index, value = int(command[1]), command[2]
            encrypted_message = insert(encrypted_message, index, value)
        elif command[0] == "ChangeAll":
            substring, replacement = command[1], command[2]
            encrypted_message = change_all(encrypted_message, substring, replacement)
    
    return encrypted_message

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    decrypted_message = decode_message(encrypted_message)
    print(f"The decrypted message is: {decrypted_message}")
