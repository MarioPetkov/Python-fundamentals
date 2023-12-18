raw_activation_key = input()

# Input validation
if not raw_activation_key.isalnum():
    exit()

while True:
    command = input()

    if command == 'Generate':
        break

    instruction = command.split('>>>')

    if instruction[0] == 'Contains':

        substring = instruction[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
            print(raw_activation_key)
        else:
            print("Substring not found!")

    elif instruction[0] == 'Flip':

        upper_or_lower = instruction[1]
        startIndex = int(instruction[2])
        endIndex = int(instruction[3])

        # Validate indices
        if 0 <= startIndex < endIndex <= len(raw_activation_key):
            if upper_or_lower == 'Upper':
                raw_activation_key = raw_activation_key[:startIndex] + raw_activation_key[startIndex:endIndex].upper() + raw_activation_key[endIndex:]
            elif upper_or_lower == 'Lower':
                raw_activation_key = raw_activation_key[:startIndex] + raw_activation_key[startIndex:endIndex].lower() + raw_activation_key[endIndex:]
            print(raw_activation_key)

    elif instruction[0] == 'Slice':

        startIndex = int(instruction[1])
        endIndex = int(instruction[2])

        # Validate indices
        if 0 <= startIndex < endIndex <= len(raw_activation_key):
            raw_activation_key = raw_activation_key[:startIndex] + raw_activation_key[endIndex:]
            print(raw_activation_key)

print(f"Your activation key is: {raw_activation_key}")
