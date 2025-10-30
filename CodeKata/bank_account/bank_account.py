from datetime import date

class BankAccount:
    """
    A simple bank account implementation that supports deposits, withdrawals,
    and printing of a formatted statement.

    Each transaction is recorded with its date, the amount (positive for deposits
    and negative for withdrawals), and the resulting balance after the operation.

    Attributes:
        balance (int): The current balance of the account.
        transactions (list[tuple[str, int, int]]): 
            A list of tuples, each representing a transaction in the format:
            (date, amount, balance_after).
    """

    def __init__(self):
        """Initializes the account with zero balance and an empty transaction history."""
        self.balance = 0
        self.transactions = []

    def deposit(self, amount: int):
        """
        Adds a positive amount to the account balance and records the transaction.

        Args:
            amount (int): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append((date.today().isoformat(), amount, self.balance))

    def withdraw(self, amount: int):
        """
        Deducts a positive amount from the account balance if sufficient funds exist.

        Args:
            amount (int): The amount to withdraw. Must be positive and ≤ current balance.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append((date.today().isoformat(), -amount, self.balance))

    def printStatement(self):
        """
        Prints a transaction statement showing the account history.

        The statement is displayed in reverse chronological order, with columns:
        Date, Amount (signed), and Balance after each transaction.

        Example Output:
            Date       || Amount || Balance
            2025-10-30 || +500    || 1500
            2025-10-29 || -200    || 1000
        """
        print("Date       || Amount || Balance")
        for d, amount, bal in reversed(self.transactions):
            print(f"{d} || {amount:+} || {bal}")
