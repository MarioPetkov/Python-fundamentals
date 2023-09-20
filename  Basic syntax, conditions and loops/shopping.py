budget = int(input())
spent = 0
while spent <= budget:
    product = input()
    if product == "End":
        print("You bought everything needed.")
        break
    spent += int(product)
else:
    print("You went in overdraft")