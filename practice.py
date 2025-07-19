#is class mae sare chize dalu ga
class NormalAccount():
    def __init__(self):
        self.account_holder=""
        self.initial_balance=0

        #use detail lene ke liye

    def create_account(self):
        self.account_holder=input("Please enter your name: ")
        self.initial_balance=int(input("Please enter the satrting balance: Rs"))
        
        #deposite ka logic

    def deposite(self):
        
        amount=int(input("How much money do you want to deposite: RS "))
        self.initial_balance+=amount
        print(f"Rs{amount} money added. Your new balance is Rs{self.initial_balance}")

       
       #withdraw ka logic
    
    def withdraw(self):
        
        amount=int(input("How much money do you want to withdraw: Rs"))
        if amount>self.initial_balance:
            print("Transaction failled due to low balance")
        else:
            self.initial_balance-=amount
            print(f"Rs{amount} withdrawn successfully. Your new balance is Rs{self.initial_balance}")

        
        #Balance check

    def display_balance(self):
        print(f"Your current balance is Rs{self.initial_balance}")


#child class
class SavingAccount(NormalAccount):
    def __init__(self):
        super().__init__()
        self.intrest_applied=5


#intrest ka logic
    def add_interest(self):
        print("Intrest of the bank balance will be added to your account")
        self.initial_balance+=self.initial_balance*(self.intrest_applied/100)
        print(f"Your new balance is Rs{self.initial_balance}")

        #special withdraw case
    
    def withdraw_scheme(self):
        amount=int(input("How much money do you want to withdraw: Rs "))
        if amount>10000:
            print("Can,t withdraw more than 10000")
        if amount>self.initial_balance:
                print("Transaction failled due to low balance")
        else:
            self.initial_balance-=amount
            print(f"Rs{amount} withdrawn successfully. Your new balance is Rs{self.initial_balance}")
        


#CLI 
print("welcome to Vansh Bank")
user=input("Sir, would you like to create a account in our bank (y or n)").strip().lower()
import os
while True:
    try:
        
        if user=="y":
            
            account_type=input("Which type of account do you want to open?\n(saving or normal)").strip().lower()
            if account_type=="saving":
                f=SavingAccount()
                f.create_account()
                f.display_balance()
                hu=input("Congratulation, Your saving account created successfully🎉\n Are you happy😍(y or n)")
                while True:
                    os.system('cls')
                    f.display_balance()
                    procedure=input("What would you like to do?\n(deposit,withdraw or exit): ").lower()
                    if procedure=="deposite":
                        f.deposite()
                    elif procedure=="withdraw":
                        f.withdraw_scheme()
                    elif procedure=="exit":
                        f.display_balance()
                        print("Thanks for visiting")
                        break
                    else:
                        print("Please enter a valid input")
                break
            if account_type=="normal":
                f=NormalAccount()
                f.create_account()
                f.display_balance()
                hu=input("Your saving account created successfully🎉\n Are you happy😍(y or n)")
                
                
                while True:
                    os.system('cls')
                    f.display_balance()
                    procedure=input("What would you like to do?\n(deposit,withdraw or exit): ").lower()
                    if procedure=="deposite":
                        f.deposite()
                    elif procedure=="withdraw":
                        f.withdraw()
                    elif procedure=="exit":
                        f.display_balance()
                        print("Thanks for visiting")
                        break
                    else:
                        ("Please enter a valid input")
                break
                
                

        else:
            print("We respect your desigion.\nSorry for inconviniance😔😔")
            break
    except(TypeError):
        print("please enter correct details")
        continue


    

        
        