concealed_message = input()
command = input().split(":|:")
while command[0] != "Reveal":
    if command[0] == "InsertSpace":
        command_index = int(command[1])
        concealed_message = concealed_message[:command_index] + " " + concealed_message[command_index:]
        print(concealed_message)

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            concealed_message += reversed_substring
            print(concealed_message)
        else: print("error")
        

    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input().split(":|:")
print(f"You have a new text message: {concealed_message}")
