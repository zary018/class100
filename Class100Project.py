class ATM:
    
    def __init__(self, pin):    
        self.p = pin

    def balance(self)  :  
        print("This is your balance --> $50,000")


    def withdraw(self):
        amount = int(input("Enter Amount of Withdrawal --> $"))
        balance = 50000 - amount
        print("This is your balance --> $" , balance)
        

    def deposit(self):
        amount = int(input("Enter Amount of Deposit --> $"))
        balance = 50000 + amount
        print("This is your balance --> $", balance)


def checkATM():
    
    pin_number  = input("Enter your PIN Number:- ")
    
    user = ATM(pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl    3.Deposit")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        user.balance()
        
    elif (activity == 2):
        user.withdraw()
    
    elif (activity == 3):
        user.deposit()

checkATM()