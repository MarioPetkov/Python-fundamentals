spell = input()
command = input().split(' ')
while command[0] != 'Abracadabra':
    if command[0] == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command[0] == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command[0] == "Illusion":
        index, letter = int(command[1]), command[2]
        if index not in range(len(spell)):
            print("The spell was too weak.")
        else:   
            spell = spell.replace(spell[index], letter, 1)
            print("Done!")
    elif command[0] == "Divination":
        first_substring, second_substring = command[1], command[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif command[0] == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
        else:
            print("The spell did not work!")
    else:
        print("The spell did not work!")
    command = input().split(' ')
