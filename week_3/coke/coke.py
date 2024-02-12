remaning_balance = 50
while True:
    user_input = int(input("Insert Coin : "))

    if user_input not in  [5,10,25]:
        print("Amount Due: 50")
        break

    else:
        remaning_balance -= user_input
        if remaning_balance > 0 :
            print(f"Amount Due: {remaning_balance}")
            continue

        elif remaning_balance <= 0:
            print(f"Change Owed: {remaning_balance - (2*remaning_balance)}")
            break





