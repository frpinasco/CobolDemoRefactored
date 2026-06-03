# Technical Architecture Document: CobolDemoRefactored

**Document ID:** CobolDemoRefactored-TAD-v1.0  
**Date:** 2026-06-03  
**Status:** Approved  
**Owner:** IT Architect

---

## 1. Overview

### 1.1 Purpose

This TAD defines the technical architecture for the Python 3.12 port of the COBOL_TEST demonstration program. It specifies the package structure, module responsibilities, inter-module relationships, testing strategy, and dependency management.

### 1.2 Technology Stack

| Concern | Choice | Version | Notes |
|---------|--------|---------|-------|
| Language | Python | 3.12 | Path: `C:\Program Files\Python314\python.exe` |
| Application type | CLI | — | Invoked via `python -m cobol_demo.main` |
| Test framework | pytest | Latest stable | No external production deps |
| Coverage | pytest-cov | Latest stable | Dev dependency only |
| VCS | Git / GitHub | — | https://github.com/frpinasco/CobolDemoRefactored |

---

## 2. Package Structure

```
CobolDemoRefactored/
├── src/
│   └── cobol_demo/
│       ├── __init__.py              # Package init (empty)
│       ├── age_classifier.py        # F-001: Age Group Classification
│       ├── countdown.py             # F-002: Countdown Loop
│       ├── fibonacci.py             # F-003: Fibonacci Sequence
│       ├── addition.py              # F-004: Two-Integer Addition
│       ├── ctest_stub.py            # F-005: External C Function Stub
│       └── main.py                  # Orchestrator: runs all features
├── tests/
│   ├── __init__.py                  # Test package init (empty)
│   ├── test_age_classifier.py       # Tests for TF-001
│   ├── test_countdown.py            # Tests for TF-002
│   ├── test_fibonacci.py            # Tests for TF-003
│   ├── test_addition.py             # Tests for TF-004
│   └── test_ctest_stub.py           # Tests for TF-005
├── artifacts/                       # SDLC artefacts (non-executable)
├── requirements.txt                 # pytest (runtime test dep)
├── requirements-dev.txt             # pytest, pytest-cov (dev/CI)
└── README.md
```

---

## 3. Module Specifications

### 3.1 `age_classifier.py` — F-001

**Responsibility:** Pure function for age group classification.

**Public API:**
```python
def classify_age(age: int) -> str:
    """Classify age into ADULT, TEEN, or CHILD.
    
    Args:
        age: Integer between 0 and 99 inclusive.
    
    Returns:
        "ADULT" if age >= 18, "TEEN" if age >= 13, else "CHILD".
    
    Raises:
        ValueError: If age is not an integer, or is outside [0, 99].
    """
```

**Decision table:**

| Condition | Output |
|-----------|--------|
| age >= 18 | "ADULT" |
| 13 <= age < 18 | "TEEN" |
| 0 <= age < 13 | "CHILD" |
| age < 0 or age > 99 or not int | ValueError |

**Dependencies:** None (stdlib only)

---

### 3.2 `countdown.py` — F-002

**Responsibility:** Generator and display function for do-while countdown.

**Public API:**
```python
from typing import Generator

def countdown(start: int = 3) -> Generator[int, None, None]:
    """Yield countdown values from start down to 1 (do-while semantics)."""

def display_countdown(start: int = 3) -> None:
    """Print 'Counting down ... N' for each value in countdown(start)."""
```

**Design notes:**
- `countdown` is a generator to enable easy testing (collect all values)
- Do-while semantics: body runs once before checking the exit condition
- Implementation: `while True: yield counter; counter -= 1; if counter == 0: break`

**Dependencies:** `typing.Generator`

---

### 3.3 `fibonacci.py` — F-003

**Responsibility:** Iterative Fibonacci generator and display function.

**Public API:**
```python
from typing import Generator

def fibonacci_sequence(count: int = 10) -> Generator[tuple[int, int], None, None]:
    """Yield (position, value) for Fibonacci positions 1..count.
    
    Uses display-before-update algorithm matching COBOL analysis expected output.
    Position 6 = 5, position 7 = 8, ..., position 10 = 34.
    """

def display_fibonacci(count: int = 10, skip: int = 5) -> None:
    """Print 'FIBONACCI N : value' for positions > skip."""
```

**Algorithm (display-before-update):**
```
nr, last = 0, 1
for i in range(1, count+1):
    yield i, nr          # display current value BEFORE update
    temp = nr
    nr = nr + last
    last = temp
```

**Full sequence for count=10:**

| i | nr (yielded) |
|---|-------------|
| 1 | 0 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 3 |
| 6 | 5 |
| 7 | 8 |
| 8 | 13 |
| 9 | 21 |
| 10 | 34 |

**Dependencies:** `typing.Generator`

---

### 3.4 `addition.py` — F-004

**Responsibility:** Input validation, addition, and result formatting.

**Public API:**
```python
def validate_integer(value: str, label: str) -> int:
    """Parse and validate a user-supplied string as an integer in [0, 99].
    
    Raises:
        ValueError: If value is non-numeric, < 0, or > 99.
    """

def add_two_integers(val1: int, val2: int) -> int:
    """Return val1 + val2."""

def format_result(val1: int, val2: int) -> str:
    """Return 'RESULT: val1 + val2 = sum'."""

def run_addition() -> None:
    """Interactive: prompt for two integers and print result."""
```

**Validation rules:**
1. Non-numeric string → `ValueError: "Input must be numeric"`
2. Integer < 0 → `ValueError: "Input must be >= 0"`
3. Integer > 99 → `ValueError: "Input must be <= 99"`

**Dependencies:** None (stdlib only)

---

### 3.5 `ctest_stub.py` — F-005

**Responsibility:** Python stub replacing COBOL `CALL 'ctest' using 1337`.

**Public API:**
```python
def ctest(value: int) -> None:
    """Stub for external C function ctest. Prints confirmation message."""
```

**Output:** `"ctest called with: {value}"`

**Dependencies:** None

---

### 3.6 `main.py` — Orchestrator

**Responsibility:** Run all features in sequence, matching COBOL execution flow.

**Execution order:**
1. Display static name (hardcoded "x444556")
2. Classify age (default 16, injectable)
3. Display countdown
4. Display Fibonacci positions 6-10
5. Run interactive addition (prompt for two integers)
6. Call ctest stub with 1337

**Public API:**
```python
def main(age: int = 16) -> None:
    """Run all COBOL demo features in sequence."""
```

---

## 4. Dependency Management

### `requirements.txt`
```
pytest
```

### `requirements-dev.txt`
```
pytest
pytest-cov
```

No third-party production dependencies. All business logic uses Python 3.12 standard library only.

---

## 5. Testing Strategy

### 5.1 Test Framework

- **Framework:** pytest
- **Coverage:** pytest-cov (`--cov=cobol_demo --cov-report=term-missing`)
- **Target:** 100% statement coverage

### 5.2 Test Design Principles

| Principle | Application |
|-----------|-------------|
| Parametric | Use `@pytest.mark.parametrize` for boundary value analysis |
| Isolation | Each test function tests one behaviour |
| Fast | No I/O blocking; all interactive I/O tested via capsys / monkeypatch |
| Readable | Test names describe the scenario being tested |

### 5.3 Test File Map

| Module | Test File | Test Count (minimum) |
|--------|-----------|---------------------|
| age_classifier.py | test_age_classifier.py | 9 (6 valid + 3 invalid) |
| countdown.py | test_countdown.py | 4 |
| fibonacci.py | test_fibonacci.py | 3 |
| addition.py | test_addition.py | 7 |
| ctest_stub.py | test_ctest_stub.py | 3 |
| **Total** | | **26 minimum** |

### 5.4 Coverage Gate

All modules must reach 100% statement coverage. The CI/CD pipeline (Stage 5) will enforce this via `--cov-fail-under=100`.

---

## 6. Execution

### Run the application
```bash
cd CobolDemoRefactored
python -m cobol_demo.main
```

### Run tests
```bash
pytest tests/ -v
```

### Run tests with coverage
```bash
pytest tests/ --cov=cobol_demo --cov-report=term-missing --cov-fail-under=100
```

---

## 7. Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Package layout | `src/cobol_demo/` | Avoids accidental imports from root; standard src layout |
| Generator for countdown/fibonacci | Yes | Separates logic from display; enables easy unit testing of sequences |
| Fibonacci algorithm | Display-before-update | Matches COBOL analysis report expected output (5,8,13,21,34) |
| Validation in addition | validate_integer() separate | Testable in isolation; reusable by main.py |
| No external deps | stdlib + pytest only | Self-contained; mirrors original COBOL's self-contained nature |
