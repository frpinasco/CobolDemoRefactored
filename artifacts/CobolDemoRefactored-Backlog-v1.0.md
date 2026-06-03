# User Story Backlog: CobolDemoRefactored

**Document ID:** CobolDemoRefactored-Backlog-v1.0  
**Date:** 2026-06-03  
**Status:** Active  
**Owner:** SDLC Pipeline Orchestrator

---

## Backlog Summary

| Story ID | Title | GitHub Issue | Priority | Status |
|----------|-------|-------------|----------|--------|
| TF-001 | Age Group Classification | #3 | High | Open |
| TF-002 | Countdown Loop | #4 | Medium | Open |
| TF-003 | Fibonacci Sequence | #5 | Medium | Open |
| TF-004 | Two-Integer Addition with Validation | #6 | High | Open |
| TF-005 | ctest Stub Function | #7 | Low | Open |

---

## TF-001: Age Group Classification

**GitHub Issue:** https://github.com/frpinasco/CobolDemoRefactored/issues/3  
**Priority:** High  
**Source Feature:** F-001  
**Module:** `src/cobol_demo/age_classifier.py`  
**Test File:** `tests/test_age_classifier.py`

### User Story

> As a user,  
> I want the system to classify an integer age value into ADULT, TEEN, or CHILD,  
> So that the original COBOL conditional decision logic (F-001) is preserved and testable in Python.

### Acceptance Criteria

| # | Given | When | Then |
|---|-------|------|------|
| AC-001-1 | age = 18 | classify_age(18) is called | Returns "ADULT" |
| AC-001-2 | age = 25 | classify_age(25) is called | Returns "ADULT" |
| AC-001-3 | age = 13 | classify_age(13) is called | Returns "TEEN" |
| AC-001-4 | age = 16 | classify_age(16) is called | Returns "TEEN" |
| AC-001-5 | age = 12 | classify_age(12) is called | Returns "CHILD" |
| AC-001-6 | age = 5 | classify_age(5) is called | Returns "CHILD" |
| AC-001-7 | age = -1 | classify_age(-1) is called | Raises ValueError |
| AC-001-8 | age = 100 | classify_age(100) is called | Raises ValueError |
| AC-001-9 | age = "abc" | classify_age("abc") is called | Raises ValueError |

### Definition of Done

- [ ] `classify_age(age: int) -> str` implemented
- [ ] All 9 acceptance criteria pass as unit tests
- [ ] 100% branch coverage for the function
- [ ] Merged to `dev` via PR

---

## TF-002: Countdown Loop

**GitHub Issue:** https://github.com/frpinasco/CobolDemoRefactored/issues/4  
**Priority:** Medium  
**Source Feature:** F-002  
**Module:** `src/cobol_demo/countdown.py`  
**Test File:** `tests/test_countdown.py`

### User Story

> As a user,  
> I want the system to count down from 3 to 1, printing each value,  
> So that the COBOL do-while loop (PERFORM WITH TEST AFTER) is faithfully reproduced in Python.

### Acceptance Criteria

| # | Given | When | Then |
|---|-------|------|------|
| AC-002-1 | start = 3 | countdown(3) is exhausted | Yields [3, 2, 1] |
| AC-002-2 | start = 1 | countdown(1) is exhausted | Yields [1] (one iteration) |
| AC-002-3 | start = 3 | display_countdown(3) is called | stdout = "Counting down ... 3\nCounting down ... 2\nCounting down ... 1\n" |
| AC-002-4 | start = 3 | countdown(3) is counted | Generator terminates after exactly 3 iterations |

### Definition of Done

- [ ] `countdown(start: int = 3) -> Generator[int, None, None]` implemented
- [ ] `display_countdown(start: int = 3) -> None` implemented
- [ ] All 4 acceptance criteria pass as unit tests
- [ ] Merged to `dev` via PR

---

## TF-003: Fibonacci Sequence

**GitHub Issue:** https://github.com/frpinasco/CobolDemoRefactored/issues/5  
**Priority:** Medium  
**Source Feature:** F-003  
**Module:** `src/cobol_demo/fibonacci.py`  
**Test File:** `tests/test_fibonacci.py`

### User Story

> As a user,  
> I want the system to generate Fibonacci values for positions 1-10 and display only positions 6-10,  
> So that the COBOL PERFORM VARYING Fibonacci logic (F-003) is reproduced with correct output.

### Acceptance Criteria

| # | Given | When | Then |
|---|-------|------|------|
| AC-003-1 | count = 10 | fibonacci_sequence(10) is exhausted | Yields [(1,0),(2,1),(3,1),(4,2),(5,3),(6,5),(7,8),(8,13),(9,21),(10,34)] |
| AC-003-2 | skip = 5 | display_fibonacci(10, skip=5) is called | stdout contains "FIBONACCI 6 : 5\nFIBONACCI 7 : 8\nFIBONACCI 8 : 13\nFIBONACCI 9 : 21\nFIBONACCI 10 : 34\n" |
| AC-003-3 | skip = 5 | display_fibonacci(10, skip=5) is called | stdout does NOT contain "FIBONACCI 1" through "FIBONACCI 5" |

### Definition of Done

- [ ] `fibonacci_sequence(count: int = 10) -> Generator[tuple[int, int], None, None]` implemented
- [ ] `display_fibonacci(count: int = 10, skip: int = 5) -> None` implemented
- [ ] All 3 acceptance criteria pass as unit tests
- [ ] Merged to `dev` via PR

---

## TF-004: Two-Integer Addition with Validation

**GitHub Issue:** https://github.com/frpinasco/CobolDemoRefactored/issues/6  
**Priority:** High  
**Source Feature:** F-004  
**Module:** `src/cobol_demo/addition.py`  
**Test File:** `tests/test_addition.py`

### User Story

> As a user,  
> I want to input two integers, have them validated against the 0-99 range, and see the result formatted,  
> So that the COBOL addition feature (F-004) is implemented with the input validation that was missing in the original.

### Acceptance Criteria

| # | Given | When | Then |
|---|-------|------|------|
| AC-004-1 | val1=25, val2=17 | format_result(25, 17) is called | Returns "RESULT: 25 + 17 = 42" |
| AC-004-2 | val1=0, val2=0 | format_result(0, 0) is called | Returns "RESULT: 0 + 0 = 0" |
| AC-004-3 | val1=99, val2=99 | format_result(99, 99) is called | Returns "RESULT: 99 + 99 = 198" |
| AC-004-4 | input = "abc" | validate_integer("abc", "test") is called | Raises ValueError |
| AC-004-5 | input = "-1" | validate_integer("-1", "test") is called | Raises ValueError |
| AC-004-6 | input = "100" | validate_integer("100", "test") is called | Raises ValueError |
| AC-004-7 | input = "50" | validate_integer("50", "test") is called | Returns 50 |

### Definition of Done

- [ ] `validate_integer(value: str, label: str) -> int` implemented
- [ ] `add_two_integers(val1: int, val2: int) -> int` implemented
- [ ] `format_result(val1: int, val2: int) -> str` implemented
- [ ] All 7 acceptance criteria pass as unit tests
- [ ] Merged to `dev` via PR

---

## TF-005: ctest Stub Function

**GitHub Issue:** https://github.com/frpinasco/CobolDemoRefactored/issues/7  
**Priority:** Low  
**Source Feature:** F-005  
**Module:** `src/cobol_demo/ctest_stub.py`  
**Test File:** `tests/test_ctest_stub.py`

### User Story

> As a developer,  
> I want a Python stub for `CALL 'ctest' using 1337`,  
> So that the external C dependency is replaced with a testable Python function that confirms it was called with the correct argument.

### Acceptance Criteria

| # | Given | When | Then |
|---|-------|------|------|
| AC-005-1 | value = 1337 | ctest(1337) is called | stdout = "ctest called with: 1337\n" |
| AC-005-2 | value = 0 | ctest(0) is called | stdout = "ctest called with: 0\n" |
| AC-005-3 | value = 42 | ctest(42) is called | stdout = "ctest called with: 42\n" |

### Definition of Done

- [ ] `ctest(value: int) -> None` implemented
- [ ] All 3 acceptance criteria pass as unit tests
- [ ] Merged to `dev` via PR
