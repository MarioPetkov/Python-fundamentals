def decrypt_message(key, message):
    decrypted_message = ""

    for counter in range(len(message)):
        character = message[counter]
        key_value = key[counter % len(key)]
        decrypted_char = chr(ord(character) - key_value)
        decrypted_message += decrypted_char

    return decrypted_message

def extract_treasure_info(decrypted_message):
    type_symbol = "&"
    coordinates_symbol_begin, coordinates_symbol_end = "<", ">"
    
    type_begin_index, type_end_index = -1, -1
    coordinates_begin_index, coordinates_end_index = -1, -1

    for i in range(len(decrypted_message)):
        if decrypted_message[i] == type_symbol:
            if type_begin_index == -1:
                type_begin_index = i
            else:
                type_end_index = i
                break

    for i in range(type_end_index + 1, len(decrypted_message)):
        if decrypted_message[i] == coordinates_symbol_begin:
            coordinates_begin_index = i
        elif decrypted_message[i] == coordinates_symbol_end:
            coordinates_end_index = i
            break

    if (type_begin_index != -1 and type_end_index != -1 and
            coordinates_begin_index != -1 and coordinates_end_index != -1):
        treasure_type = decrypted_message[type_begin_index + 1:type_end_index]
        coordinates = decrypted_message[coordinates_begin_index + 1:coordinates_end_index]
        return treasure_type, coordinates
    else:
        return None, None

def main():
    # Read the key sequence as a list of integers
    key_sequence = list(map(int, input("Enter the key (numbers separated by space): ").split()))

    # Initialize encrypted_message with the first input
    encrypted_message = input()

    # Continue reading messages until "find" is encountered
    while encrypted_message != "find":
        # Decrypt the message
        decrypted_message = decrypt_message(key_sequence, encrypted_message)

        # Extract type and coordinates
        treasure_type, coordinates = extract_treasure_info(decrypted_message)

        # Print the result
        if treasure_type is not None and coordinates is not None:
            print(f"Found {treasure_type} at {coordinates}.")
        else:
            print("Invalid format in the decrypted message.")

        # Read the next encrypted message
        encrypted_message = input()

if __name__ == "__main__":
    main()
