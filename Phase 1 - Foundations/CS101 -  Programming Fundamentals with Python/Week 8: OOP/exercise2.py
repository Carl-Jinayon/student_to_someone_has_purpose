"""
Exercise 2 (Encapsulation):
Define a class BankAccount with:

1. Private attribute _balance (initial 0).
2. Methods: deposit(amount), withdraw(amount), get_balance().
3. deposit and withdraw should return True on success, False on failure.
"""

class BankAccount:

    class NegativeBalanceError(Exception):
        def __init__(self, message="Insufficient balance"):
            self.message = message
            super().__init__(message)

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.__balance:
                raise self.NegativeBalanceError(f"Cannot withdraw ${amount}: Balance is ${self.__balance}")
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"BankAccount(Balance: {self.__balance:.2f})"

my_account = BankAccount()

while True:
    print("\n1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("=====================")
            print(f"Current Balance: ${my_account.get_balance():.2f}")
            print("=====================")

        elif choice == 2:
            amount = float(input("Enter amount: "))
            print("=====================")
            if my_account.deposit(amount):
                print("Deposit Successful.")
            else:
                print("Invalid amount (must be positive).")
            print("=====================")
        
        elif choice == 3:
            amount = float(input("Enter amount: "))
            print("=====================")
            try:
                if my_account.withdraw(amount):
                    print("Withdraw successful.")
                else:
                    print("Invalid amount.")
            except BankAccount.NegativeBalanceError as e:
                print(f"{e}")
            print("=====================")
        
        elif choice == 4:
            break
        
    except ValueError:
        print("=====================")
        print("Enter a valid number.")
        print("=====================")
