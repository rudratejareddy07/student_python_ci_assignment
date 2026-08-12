# Student Python CI Assignment

This repository is intentionally supplied with a **low test-coverage baseline**.

Your task is to improve the automated test suite so that the GitHub Actions
coverage gate reaches **at least 80%**.

## Assignment requirements

The GitHub Actions workflow in `.github/workflows/ci.yml` performs these gates:

1. Ruff lint check
2. Pytest with a coverage gate of 80%
3. Bandit security scan
4. Build the Python wheel

The initial tests intentionally cover only a small portion of the application.
Do **not** change the coverage threshold in the workflow.

### Student goal

Increase test coverage from the initial low baseline to **90% or higher**.

The workflow will accept anything at or above 80%, but the expected student
target is 90%.

## Run locally

```bash
python -m pip install -r requirements.txt
pip install -e .
pytest --cov=student_account --cov-report=term-missing --cov-fail-under=80
ruff check .
bandit -r src
python -m build --wheel
```

## Expected project structure

```text
student_python_ci_assignment/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── student_account/
│       ├── __init__.py
│       └── account.py
├── tests/
│   └── test_account.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Student instructions

Add tests. Do not weaken or remove the CI gates. Do not modify application code
just to make the coverage number pass.
