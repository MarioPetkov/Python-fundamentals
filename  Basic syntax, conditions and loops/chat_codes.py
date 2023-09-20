messages_sent = int(input())
for i in range(messages_sent):
    num = int(input())
    if num == 88:
        print("Hello")
    elif num == 86:
        print("How are you?")
    elif num < 86:
        print("GREAT!")
    elif num > 88:
        print("Bye.")