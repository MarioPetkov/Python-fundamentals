import re

def is_valid_message(message):
    pattern = re.compile(r'^([*@])([A-Z][a-z]{2,})\1: \[([A-Za-z])\|\]|\[([A-Za-z])\|\]|\[([A-Za-z])\|\]$')

    match = pattern.match(message)

    if match:
        tag_char = match.group(1)
        tag = match.group(2)
        group1 = match.group(3)
        group2 = match.group(4)
        group3 = match.group(5)

        if (group1 or group2 or group3) and (group1 != group2 and group2 != group3 and group1 != group3):
            return True, tag_char, tag, ord(group1), ord(group2), ord(group3)

    return False, None, None, None, None, None

def encrypt_message(tag_char, tag, num1, num2, num3):
    encrypted_message = f"{tag}: {num1} {num2} {num3}"
    return encrypted_message

def main():
    message = input("Enter your message: ")
    
    is_valid, tag_char, tag, num1, num2, num3 = is_valid_message(message)

    if is_valid:
        encrypted_message = encrypt_message(tag_char, tag, num1, num2, num3)
        print(encrypted_message)
    else:
        print("Valid message not found!")

if __name__ == "__main__":
    main()
    