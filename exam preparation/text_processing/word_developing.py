word = ''
index_list = []

while True:
    command = input().split(' ')

    if command[0] == "End":
        break

    if command[0] == 'Add':
        substring = command[1]
        word += substring

    elif command[0] == 'Upgrade':
        char = command[1]
        word = word.replace(char, chr(ord(char) + 1))

    elif command[0] == 'Index':
        char = command[1]
        if char in word:
            indices = [index for index, letter in enumerate(word) if letter == char]
            if indices:
                print(' '.join(map(str, indices)))
            else:
                print('None')
        else:
            print('None')

    elif command[0] == 'Remove':
        substring = command[1]
        word = word.replace(substring, '')

    elif command[0] == 'Print':
        print(word)
