# Student Assignment: Raise Test Coverage

## Starting point

The repository contains an OOP-based `BankAccount` class and only a minimal
test suite. The supplied tests intentionally exercise only a small portion of
the implementation.

## Your task

Increase automated test coverage to **90% or higher**.

The CI workflow enforces a minimum coverage gate of **80%**.

You must:

- Add meaningful pytest test cases.
- Cover normal and error/edge cases.
- Keep the existing 80% coverage gate unchanged.
- Keep Ruff linting enabled.
- Keep Bandit enabled.
- Do not delete or bypass existing gates.
- Do not modify production code merely to avoid testing it.

## Suggested areas to test

Consider testing:

- account creation
- invalid owner names
- negative opening balances
- deposits
- invalid deposits
- withdrawals
- insufficient funds
- transaction counts
- transfers
- invalid transfer targets
- monthly interest
- invalid interest rates
- statements
- empty transaction statements

## Success criteria

The GitHub Actions workflow should finish successfully.

The most important coverage command is:

```bash
pytest --cov=student_account --cov-report=term-missing --cov-fail-under=80
```

Aim for **90%+**, not merely 80%.
