balance=1000
while True:
    type=input("Enter the Type credit / debit :")
    if (type == "stop"):
        break
    elif(type=="credit"):
        credit_amount=int(input("Enter the credit Amount :"))
        balance=balance+credit_amount;
        print(f"The current Balance is {balance}")

    elif(type=="debit"):
        debit_amount=int(input("Enter the Debit Amount :"))
        if(balance>debit_amount):
            balance=balance-debit_amount
            print(f"Amount debited and the current balance is {balance}")
        else:
            print("insafisent balance")

    else:
        print(f"Balance :{balance}")