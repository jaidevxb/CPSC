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

