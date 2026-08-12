import time

print("Please insert your CARD")
time.sleep(4)

password=1234

balance=5000
transaction=[]

while True:
    
    print("""
        1 == Account Balance Inquiry
        2 == Cash Withdrawal
        3 == Cash deposit
        4 == PIN change
        5 == Transaction History
        6 == Exit                     
        """)
    
    try:
        option=int(input("Please enter your choice "))

    except:
        print("Please enter valid option")
    
    pin=int(input("Enter your atm pin "))
    if pin == password:
        
        
        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw_amount "))
            balance = balance-withdraw_amount
            transaction.append(f"${withdraw_amount} debited")
            print(f"{withdraw_amount} is debited from your account")
            print(f"your balance is {balance}")

        elif option == 3:
            deposit_amount=int(input("Please input deposit_amount "))
            balance=balance+deposit_amount
            transaction.append(f"${deposit_amount} credited")
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")

        elif option == 4:
            new=int(input("Enter new PIN "))
            password = new
            print("PIN has been updated")
        
        elif option == 5:    
            print("Your transaction history is:\n")
            print("\n".join(transaction))  #It shows the remaining balance after transaction in history.Join list elements into a single string

        else:
            print("Thank You!")
            break

         
    else:
        print("Wrong pin try again")
