class BankAccount:
    """Simple bank account used for the CI/testing assignment."""

    def __init__(self, owner: str, opening_balance: float = 0.0):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty.")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.owner = owner
        self._balance = float(opening_balance)
        self._transactions = []

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def transaction_count(self) -> int:
        return len(self._transactions)

    def deposit(self, amount: float) -> float:
        self._validate_amount(amount)
        self._balance += amount
        self._transactions.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount: float) -> float:
        self._validate_amount(amount)

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount
        self._transactions.append(("withdraw", amount))
        return self._balance

    def transfer_to(self, other: "BankAccount", amount: float) -> float:
        if not isinstance(other, BankAccount):
            raise TypeError("Target must be a BankAccount.")

        self.withdraw(amount)
        other.deposit(amount)
        return self._balance

    def monthly_interest(self, annual_rate: float) -> float:
        if annual_rate < 0:
            raise ValueError("Annual rate cannot be negative.")

        interest = self._balance * annual_rate / 12
        self._balance += interest
        self._transactions.append(("interest", interest))
        return interest

    def statement(self) -> str:
        lines = [
            f"Owner: {self.owner}",
            f"Balance: {self._balance:.2f}",
            f"Transactions: {len(self._transactions)}",
        ]

        if not self._transactions:
            lines.append("No transactions.")

        return "\n".join(lines)

    def _validate_amount(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
