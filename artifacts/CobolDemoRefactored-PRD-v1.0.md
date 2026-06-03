# Product Requirements Document: COBOL Demo Refactored — Python 3.12 Port

**Project Title:** COBOL Demo Refactored — Python 3.12 Port  
**Document ID:** CobolDemoRefactored-PRD-v1.0  
**Date:** 2026-06-03  
**Status:** Approved  
**Owner:** SDLC Pipeline Orchestrator

---

## 1. Purpose & Scope

### 1.1 Background

The `COBOL_TEST` program is a demonstration utility that validates multiple COBOL language features: conditional decision logic, loop constructs (do-while and PERFORM VARYING), iterative mathematical computation, interactive user input with arithmetic, and external C function interoperability.

### 1.2 Purpose

Modernize the `COBOL_TEST` program into idiomatic Python 3.12, preserving all original behavioural features while applying contemporary software engineering practices: input validation, testability, parametric inputs, and 100% unit test coverage.

### 1.3 Scope

- Python 3.12 CLI application
- Five features (F-001 to F-005) ported from COBOL source
- Enhancement: F-001 age made injectable (not hardcoded)
- Enhancement: F-004 input validation added
- Enhancement: F-005 replaced with a Python stub function
- Unit tests with pytest achieving 100% coverage target

### 1.4 Out of Scope

- Web UI or API layer
- Database integration
- Actual C library linkage (F-005 is a stub)
- COBOL runtime or transpilation

---

## 2. Stakeholders

| Role | Name | Responsibility |
|------|------|----------------|
| Product Owner | SDLC Orchestrator | Feature approval and acceptance |
| Developer | Senior Lead Developer | Implementation and unit tests |
| QA | Senior Lead Tester | Test design and execution |
| DevOps | Senior DevOps Engineer | CI/CD pipeline |

---

## 3. Feature Requirements

### PR-001: Age Group Classification (F-001)

**Priority:** High  
**Source:** COBOL Feature F-001, BR-001

**Description:**  
The system shall classify an integer age value into one of three groups:

| Condition | Output |
|-----------|--------|
| age >= 18 | "ADULT" |
| age >= 13 and age < 18 | "TEEN" |
| age < 13 | "CHILD" |

**Enhancement PR-001a:**  
Age shall be accepted as an injectable parameter, not hardcoded. The function signature shall be `classify_age(age: int) -> str`.

**Acceptance Criteria:**

| Input | Expected Output |
|-------|----------------|
| 18 | "ADULT" |
| 25 | "ADULT" |
| 13 | "TEEN" |
| 16 | "TEEN" |
| 12 | "CHILD" |
| 5 | "CHILD" |
| -1 | ValueError raised |
| 100 | ValueError raised |
| "abc" | ValueError raised |

---

### PR-002: Countdown Loop (F-002)

**Priority:** Medium  
**Source:** COBOL Feature F-002, BR-002

**Description:**  
The system shall count down from 3 to 1 (inclusive), printing a line for each value. The loop shall exhibit do-while semantics: the body executes at least once before the exit condition is checked.

**Output format per iteration:** `"Counting down ... N"`

**Acceptance Criteria:**

| Start Value | Expected Output Lines |
|-------------|----------------------|
| 3 | "Counting down ... 3", "Counting down ... 2", "Counting down ... 1" |
| 1 | "Counting down ... 1" (single iteration, do-while) |

---

### PR-003: Fibonacci Sequence (F-003)

**Priority:** Medium  
**Source:** COBOL Feature F-003, BR-003

**Description:**  
The system shall generate the Fibonacci sequence for positions 1 through 10 and display only positions 6 through 10.

**Display format:** `"FIBONACCI N : value"`

**Acceptance Criteria:**

| Position | Value | Output |
|----------|-------|--------|
| 6 | 5 | "FIBONACCI 6 : 5" |
| 7 | 8 | "FIBONACCI 7 : 8" |
| 8 | 13 | "FIBONACCI 8 : 13" |
| 9 | 21 | "FIBONACCI 9 : 21" |
| 10 | 34 | "FIBONACCI 10 : 34" |

Positions 1-5 are computed but not displayed.

---

### PR-004: Two-Integer Addition with Validation (F-004)

**Priority:** High  
**Source:** COBOL Feature F-004, BR-004, Enhancement BR-004a

**Description:**  
The system shall prompt for two integers (0-99 each), validate each input, add them, and display the result.

**Display format:** `"RESULT: val1 + val2 = sum"`

**Enhancement PR-004a (Input Validation):**  
The system shall reject non-numeric input and out-of-range values (< 0 or > 99), displaying an appropriate error message and re-prompting until valid input is provided.

**Acceptance Criteria:**

| Input 1 | Input 2 | Expected Output |
|---------|---------|----------------|
| 25 | 17 | "RESULT: 25 + 17 = 42" |
| 0 | 0 | "RESULT: 0 + 0 = 0" |
| 99 | 99 | "RESULT: 99 + 99 = 198" |
| "abc" | — | ValueError raised |
| -1 | — | ValueError raised |
| 100 | — | ValueError raised |

---

### PR-005: External C Function Stub (F-005)

**Priority:** Low  
**Source:** COBOL Feature F-005, BR-005

**Description:**  
The original COBOL program called an external C function `ctest` with argument 1337. In the Python port, this shall be implemented as a pure Python stub function that prints a confirmation message.

**Function signature:** `ctest(value: int) -> None`

**Output:** `"ctest called with: {value}"`

**Acceptance Criteria:**

| Input | Expected Output |
|-------|----------------|
| 1337 | "ctest called with: 1337" |
| 0 | "ctest called with: 0" |
| 42 | "ctest called with: 42" |

---

## 4. Non-Functional Requirements

### NFR-001: Language

- Python 3.12 (path: `C:\Program Files\Python314\python.exe`)
- No external runtime dependencies beyond Python standard library

### NFR-002: Application Type

- CLI application executed via `python -m cobol_demo.main`
- No GUI, web, or API interface

### NFR-003: Testing

- Test framework: pytest
- Coverage tool: pytest-cov
- Coverage target: 100% statement coverage across all modules
- All tests parametric where multiple input/output pairs exist

### NFR-004: Dependencies

- `requirements.txt`: `pytest` only
- `requirements-dev.txt`: `pytest`, `pytest-cov`
- No third-party libraries beyond pytest in production code

### NFR-005: Code Quality

- Type hints on all public functions
- Docstrings on all public functions
- Modules named per architecture document (TAD)

### NFR-006: Repository

- GitHub: https://github.com/frpinasco/CobolDemoRefactored
- Branching: `main` (stable) → `dev` (integration) → `feature/TF-00N` (stories)

---

## 5. Constraints

1. The Fibonacci output values (positions 6-10 → 5, 8, 13, 21, 34) are defined by the analysis report's expected output and acceptance criteria table — this is the normative specification.
2. The age parameter for F-001 in the main orchestration shall default to 16 (matching the original COBOL hardcoded value) but be injectable.
3. F-005 shall not link to any actual C library.

---

## 6. Acceptance Definition

The project is accepted when:
1. All five features are implemented in Python 3.12 per the specifications above.
2. All unit tests pass with `pytest`.
3. Code coverage reaches 100% of statements.
4. The application runs end-to-end via `python -m cobol_demo.main`.
