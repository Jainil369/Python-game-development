class Account():
    def __init__(self,balance,accountpin,document):
        self.balance = balance
        self.accountpin = accountpin
        self.document = document 
    def checkbalance(self):
        print("Your balance is: ", self.balance)
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficent funds")
        else:
            self.balance -= amount
            self.checkbalance()   
    def deposit(self, amount):
        self.balance += amount
        self.checkbalance()



account123 = Account(50000,3554,"ID5555")    


print("What would you like to do?")
print("1. Check balance")
print("2. Withdraw")
print("3. Deposit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1 :
        account123.checkbalance()
    elif choice == 2:
        amount = int(input("Enter the amount to withdraw:"))
        if amount > 100000:
            verification = input("Enter bank document id:")
            if verification == account123.document:
                account123.withdraw(amount)
            else:
                print("Verification failed. Transaction cancelled.") 
        else:
            account123.withdraw(amount)           
    elif choice == 3:
        amount = int(input("Enter the amount to deposit:"))
           
        if amount > 100000:
            verifications = input("Enter account pin:")
            if verifications == account123.accountpin:
                account123.deposir(amount)
            else:
                print("Verification failed. Transaction cancelled.")
        else:
            account123.deposit(amount)        

