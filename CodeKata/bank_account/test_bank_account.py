from bank_account import BankAccount
import re

def test_bank_account_deposit_and_withdraw(capsys):
    account = BankAccount()
    account.deposit(1000)
    account.deposit(2000)
    account.withdraw(500)
    account.printStatement()

    captured = capsys.readouterr().out.strip()
    lines = captured.split("\n")

    # Header check
    assert lines[0].startswith("Date")
    assert len(lines) == 4  # 1 header + 3 transactions

    # Latest transaction first (withdrawal)
    assert "-" in lines[1]  
    assert "+" in lines[3]  

def test_negative_deposit():
    account = BankAccount()
    try:
        account.deposit(-100)
    except ValueError as e:
        assert str(e) == "Deposit amount must be positive."

def test_zero_deposit():
    account = BankAccount()
    try:
        account.deposit(0)
    except ValueError as e:
        assert "positive" in str(e)

def test_insufficient_funds():
    account = BankAccount()
    account.deposit(100)
    try:
        account.withdraw(200)
    except ValueError as e:
        assert str(e) == "Insufficient funds."

def test_zero_withdraw():
    account = BankAccount()
    account.deposit(500)
    try:
        account.withdraw(0)
    except ValueError as e:
        assert "positive" in str(e)

def test_print_statement_format(capsys):
    account = BankAccount()
    account.deposit(500)
    account.printStatement()
    captured = capsys.readouterr().out.strip()

    # Check correct column headers
    assert re.match(r"Date\s+\|\|\s+Amount\s+\|\|\s+Balance", captured)
    # One header + one transaction
    assert len(captured.split("\n")) == 2

def test_empty_account_statement(capsys):
    account = BankAccount()
    account.printStatement()
    out = capsys.readouterr().out.strip()
    assert out == "Date       || Amount || Balance"


def test_running_balance_calculation(capsys):
    account = BankAccount()
    account.deposit(1000)
    account.withdraw(400)
    account.deposit(200)

    assert account.balance == 800  # 1000 - 400 + 200

def test_negative_withdraw():
    account = BankAccount()
    account.deposit(100)
    try:
        account.withdraw(-50)
    except ValueError as e:
        assert str(e) == "Withdraw amount must be positive."

def test_statement_order_is_latest_first(capsys):
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    account.deposit(25)
    account.printStatement()

    captured = capsys.readouterr().out.strip().split("\n")[1:]  # Skip header
    first_line = captured[0]
    last_line = captured[-1]

    # Latest should be last deposit (+25)
    assert "+25" in first_line
    # Oldest should be first deposit (+100)
    assert "+100" in last_line

def test_balance_never_negative():
    account = BankAccount()
    account.deposit(100)
    try:
        account.withdraw(200)
    except ValueError:
        pass
    assert account.balance == 100  # Still the same, withdrawal didn’t happen


def test_initial_state():
    account = BankAccount()
    assert account.balance == 0
    assert account.transactions == []


def test_transaction_record_details():
    account = BankAccount()
    account.deposit(500)
    account.withdraw(100)

    transactions = account.transactions
    assert len(transactions) == 2

    # Check tuple structure: (date, amount, balance)
    for t in transactions:
        assert len(t) == 3
        assert isinstance(t[0], str)  # date
        assert isinstance(t[1], int)
        assert isinstance(t[2], int)
