#Question-10: Simple ATM Simulator

balance = 10000  # Initial balance

while True:
    print("\n===ATM SIMULATOR===")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    choice=int(input("Enter your choice: "))

    #1.Check Balance
    if choice==1:
        print("Current Balance: ₹",balance)

    #2.Deposit Money
    elif choice==2:
        amount=int(input("Enter amount to deposit: ₹"))
        if amount>0:
            balance+=amount
            print("Deposit successful")
            print("Updated Balance: ₹",balance)
        else:
            print("Invalid deposit amount")

    #3.Withdraw money
    elif choice==3:
        amount=int(input("Enter amount to withdraw: ₹"))
        if amount<=0:
            print("Invalid withdrawal amount")
        elif balance-amount<500:
            print("Minimum balance ₹500 must be maintained")
        else:
            balance-=amount
            print("Withdrawal successful")
            print("Updated Balance: ₹",balance)

    #4.Exit
    elif choice==4:
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")