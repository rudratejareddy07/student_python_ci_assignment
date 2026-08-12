import pytest
from student_account import BankAccount


def test_init_valid_account():
    account = BankAccount("Alice", 100)

    assert account.owner == "Alice"
    assert account.balance == 100.0
    assert account.transaction_count == 0


def test_init_empty_owner_raises_value_error():
    with pytest.raises(ValueError, match="Owner name cannot be empty"):
        BankAccount("   ")


def test_init_negative_balance_raises_value_error():
    with pytest.raises(ValueError, match="Opening balance cannot be negative"):
        BankAccount("Alice", -50)


def test_deposit_increases_balance():
    account = BankAccount("Alice", 100)

    new_balance = account.deposit(50)

    assert new_balance == 150.0
    assert account.balance == 150.0
    assert account.transaction_count == 1


def test_deposit_zero_or_negative_amount_raises_value_error():
    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        account.deposit(0)

    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        account.deposit(-10)


def test_withdraw_decreases_balance():
    account = BankAccount("Alice", 100)

    new_balance = account.withdraw(30)

    assert new_balance == 70.0
    assert account.balance == 70.0
    assert account.transaction_count == 1


def test_withdraw_insufficient_funds_raises_value_error():
    account = BankAccount("Alice", 50)

    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(100)


def test_transfer_to_other_account_updates_balances():
    alice = BankAccount("Alice", 200)
    bob = BankAccount("Bob", 50)

    remaining_balance = alice.transfer_to(bob, 75)

    assert remaining_balance == 125.0
    assert alice.balance == 125.0
    assert bob.balance == 125.0
    assert alice.transaction_count == 1
    assert bob.transaction_count == 1


def test_transfer_to_non_bank_account_raises_type_error():
    alice = BankAccount("Alice", 100)

    with pytest.raises(TypeError, match="Target must be a BankAccount"):
        alice.transfer_to(object(), 10)


def test_monthly_interest_applies_interest():
    account = BankAccount("Alice", 1200)

    interest = account.monthly_interest(0.06)

    assert interest == 6.0
    assert account.balance == 1206.0
    assert account.transaction_count == 1


def test_monthly_interest_negative_rate_raises_value_error():
    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError, match="Annual rate cannot be negative"):
        account.monthly_interest(-0.01)


def test_statement_no_transactions_includes_no_transactions_message():
    account = BankAccount("Alice", 100)

    statement = account.statement()

    assert "Owner: Alice" in statement
    assert "Balance: 100.00" in statement
    assert "Transactions: 0" in statement
    assert "No transactions." in statement


def test_statement_with_transactions_includes_transaction_count():
    account = BankAccount("Alice", 100)
    account.deposit(50)
    account.withdraw(20)

    statement = account.statement()

    assert "Transactions: 2" in statement
    assert "No transactions." not in statement
