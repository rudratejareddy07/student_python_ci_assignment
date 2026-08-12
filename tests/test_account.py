from student_account import BankAccount


def test_deposit_increases_balance():
    account = BankAccount("Alice", 100)
    assert account.deposit(50) == 150
