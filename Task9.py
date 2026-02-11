class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance.")
        
        self.balance -= amount
        return self.balance


account = BankAccount(100)

try:
    amount = float(input("Enter withdrawal amount: "))
    remaining = account.withdraw(amount)
except ValueError as e:
    print("Error:", e)
except InsufficientBalanceError as e:
    print("Error:", e)
else:
    print("Remaining balance:", remaining)
