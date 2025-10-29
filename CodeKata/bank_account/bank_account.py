from datetime import date

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []  # Each item: (date, amount, balance_after)

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append((date.today().isoformat(), amount, self.balance))

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append((date.today().isoformat(), -amount, self.balance))

    def printStatement(self):
        print("Date       || Amount || Balance")
        # Print in reverse order (most recent first)
        for d, amount, bal in reversed(self.transactions):
            print(f"{d} || {amount:+} || {bal}")
