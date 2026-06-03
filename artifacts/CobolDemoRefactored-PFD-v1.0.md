# Product Feature Document: CobolDemoRefactored

**Document ID:** CobolDemoRefactored-PFD-v1.0  
**Date:** 2026-06-03  
**Status:** Approved  
**Owner:** Functional Analyst

---

## Overview

This PFD defines the five product features for the Python 3.12 refactoring of the COBOL_TEST program, along with their acceptance criteria, input/output contracts, and edge cases.

---

## Feature PF-001: Age Group Classification

**Story ID:** TF-001  
**Source:** COBOL F-001  
**Priority:** High  
**Module:** `src/cobol_demo/age_classifier.py`

### Description

A pure function `classify_age(age: int) -> str` that classifies an integer age into one of three groups.

### Input/Output Contract

| Parameter | Type | Range | Notes |
|-----------|------|-------|-------|
| age | int | 0–99 | Must be integer, inclusive bounds |
| return | str | "ADULT" / "TEEN" / "CHILD" | |

### Business Rules

| Rule | Condition | Output |
|------|-----------|--------|
| BR-001-A | age >= 18 | "ADULT" |
| BR-001-B | age >= 13 and age < 18 | "TEEN" |
| BR-001-C | age < 13 | "CHILD" |

### Validation Rules

| Rule | Condition | Response |
|------|-----------|----------|
| VR-001-1 | age is not int | raise ValueError |
| VR-001-2 | age < 0 | raise ValueError |
| VR-001-3 | age > 99 | raise ValueError |

### Acceptance Criteria

```gherkin
Given an age of 18, when classify_age is called, then "ADULT" is returned
Given an age of 25, when classify_age is called, then "ADULT" is returned
Given an age of 13, when classify_age is called, then "TEEN" is returned
Given an age of 16, when classify_age is called, then "TEEN" is returned
Given an age of 12, when classify_age is called, then "CHILD" is returned
Given an age of 5, when classify_age is called, then "CHILD" is returned
Given an age of -1, when classify_age is called, then ValueError is raised
Given an age of 100, when classify_age is called, then ValueError is raised
Given a non-integer "abc", when classify_age is called, then ValueError is raised
```

---

## Feature PF-002: Countdown Loop

**Story ID:** TF-002  
**Source:** COBOL F-002  
**Priority:** Medium  
**Module:** `src/cobol_demo/countdown.py`

### Description

A generator function `countdown(start: int = 3)` that yields integer values from `start` down to 1 inclusive, with do-while semantics (at least one yield even if start <= 1). A `display_countdown` function prints each value.

### Input/Output Contract

| Function | Parameter | Type | Default | Notes |
|----------|-----------|------|---------|-------|
| countdown | start | int | 3 | Generator, yields from start down to 1 |
| display_countdown | start | int | 3 | Prints "Counting down ... N" per value |

### Behavioural Rules

| Rule | Condition | Behaviour |
|------|-----------|-----------|
| BR-002-A | start = 3 | Yields [3, 2, 1] — 3 iterations |
| BR-002-B | start = 1 | Yields [1] — 1 iteration (do-while) |
| BR-002-C | General | Yields [start, start-1, ..., 1] |

### Acceptance Criteria

```gherkin
Given countdown(3), when all values are collected, then [3, 2, 1] is returned
Given countdown(1), when all values are collected, then [1] is returned (do-while)
Given display_countdown(3), when called, then stdout contains "Counting down ... 3\nCounting down ... 2\nCounting down ... 1\n"
```

---

## Feature PF-003: Fibonacci Sequence

**Story ID:** TF-003  
**Source:** COBOL F-003  
**Priority:** Medium  
**Module:** `src/cobol_demo/fibonacci.py`

### Description

A generator function `fibonacci_sequence(count: int = 10)` that yields `(position, value)` tuples for positions 1 through `count`. A `display_fibonacci` function prints positions above `skip` (default 5).

The algorithm uses display-before-update semantics matching the COBOL analysis report expected output.

### Input/Output Contract

| Function | Parameter | Default | Notes |
|----------|-----------|---------|-------|
| fibonacci_sequence | count | 10 | Yields (pos, val) tuples |
| display_fibonacci | count | 10 | Prints FIBONACCI lines |
| display_fibonacci | skip | 5 | Only print when pos > skip |

### Behavioural Rules (Full Sequence for count=10)

| Position | Value | Displayed? |
|----------|-------|-----------|
| 1 | 0 | No |
| 2 | 1 | No |
| 3 | 1 | No |
| 4 | 2 | No |
| 5 | 3 | No |
| 6 | 5 | Yes — "FIBONACCI 6 : 5" |
| 7 | 8 | Yes — "FIBONACCI 7 : 8" |
| 8 | 13 | Yes — "FIBONACCI 8 : 13" |
| 9 | 21 | Yes — "FIBONACCI 9 : 21" |
| 10 | 34 | Yes — "FIBONACCI 10 : 34" |

### Acceptance Criteria

```gherkin
Given fibonacci_sequence(10), when all (pos, val) pairs are collected,
  then they equal [(1,0),(2,1),(3,1),(4,2),(5,3),(6,5),(7,8),(8,13),(9,21),(10,34)]
Given display_fibonacci(10, skip=5), when called,
  then stdout contains exactly the 5 lines: FIBONACCI 6:5 through FIBONACCI 10:34
```

---

## Feature PF-004: Two-Integer Addition with Validation

**Story ID:** TF-004  
**Source:** COBOL F-004  
**Priority:** High  
**Module:** `src/cobol_demo/addition.py`

### Description

Functions to validate integer inputs (0–99), perform addition, and display the result.

`validate_integer(value: str, label: str) -> int` — parse and validate  
`add_two_integers(val1: int, val2: int) -> int` — add  
`format_result(val1: int, val2: int) -> str` — format output

### Input/Output Contract

| Function | Input | Output |
|----------|-------|--------|
| validate_integer(s, label) | string from user | int in [0,99] or ValueError |
| add_two_integers(a, b) | two validated ints | their sum |
| format_result(a, b) | two ints | "RESULT: a + b = sum" |

### Validation Rules

| Rule | Condition | Response |
|------|-----------|----------|
| VR-004-1 | Input is not numeric | raise ValueError |
| VR-004-2 | Input < 0 | raise ValueError |
| VR-004-3 | Input > 99 | raise ValueError |

### Acceptance Criteria

```gherkin
Given val1=25, val2=17, when format_result is called, then "RESULT: 25 + 17 = 42"
Given val1=0, val2=0, when format_result is called, then "RESULT: 0 + 0 = 0"
Given val1=99, val2=99, when format_result is called, then "RESULT: 99 + 99 = 198"
Given input "abc", when validate_integer is called, then ValueError is raised
Given input "-1", when validate_integer is called, then ValueError is raised
Given input "100", when validate_integer is called, then ValueError is raised
```

---

## Feature PF-005: External C Function Stub

**Story ID:** TF-005  
**Source:** COBOL F-005  
**Priority:** Low  
**Module:** `src/cobol_demo/ctest_stub.py`

### Description

Python stub replacing the COBOL `CALL 'ctest' using 1337`. The function `ctest(value: int) -> None` prints a confirmation message.

### Input/Output Contract

| Parameter | Type | Notes |
|-----------|------|-------|
| value | int | Any integer |
| return | None | Prints to stdout |
| stdout | str | "ctest called with: {value}" |

### Acceptance Criteria

```gherkin
Given ctest(1337), when called, then stdout contains "ctest called with: 1337"
Given ctest(0), when called, then stdout contains "ctest called with: 0"
Given ctest(42), when called, then stdout contains "ctest called with: 42"
```
