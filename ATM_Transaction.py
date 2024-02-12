class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}, New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdraw ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
        

def main():
    atm = ATM()
    
    while True:
        print("\nATM Transaction Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            print("Balance: $" + str(atm.check_balance()))
        elif choice == 2:
            amount = float(input("Enter deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye")
            break;
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
            

if __name__ == "__main__":
    main()