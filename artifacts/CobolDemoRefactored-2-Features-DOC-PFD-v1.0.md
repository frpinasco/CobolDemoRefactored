# Product Feature Document — CobolDemoRefactored

**Version:** 1.0
**Date:** June 24, 2026
**Source:** CobolDemoRefactored-1-Product-DOC-PRD-v1.0.md

## Executive Summary

CobolDemoRefactored is a modern reimplementation of a legacy COBOL demonstration program. Analysis of the PRD identified **5 features** across age classification, countdown, Fibonacci generation, interactive addition, and external function interop, decomposed into **11 user stories**. One assumption was made regarding the nature of the external function interop mechanism (see Assumptions section).

## Assumptions & Clarifications

1. The PRD states "Invoke an external/native function by name with a numeric argument" (REQ-007) but does not specify the mechanism. **Assumed:** for MVP, the external function is a separately compiled executable or script invoked via system call with argument passing and return code capture. The exact mechanism (shared library, subprocess, HTTP call) is deferred to the IT Architect in Stage 3.

## Feature Index

| Feature ID | Feature Name | Priority | # Stories | Feature Complete When |
|------------|-------------|----------|-----------|-----------------------|
| F-001 | Age Group Classification | Must Have | 2 | All 2 stories Done |
| F-002 | Countdown | Must Have | 2 | All 2 stories Done |
| F-003 | Fibonacci Sequence Generator | Must Have | 3 | All 3 stories Done |
| F-004 | Interactive Two-Number Addition | Must Have | 2 | All 2 stories Done |
| F-005 | External Function Interop | Should Have | 2 | All 2 stories Done |

## Features

---

## Feature: Age Group Classification

**Feature ID:** F-001
**PRD Reference:** REQ-001, REQ-017
**Priority:** Must Have

### Description
Given a numeric age (0-99), classifies it into ADULT (>=18), TEEN (>=13), or CHILD (<13). Thresholds are hardcoded for MVP; configurable in a future phase.

### Business Value
This is the simplest conditional-logic demonstration in the COBOL original. Rebuilding it in a modern language demonstrates how nested IF/ELSE maps to idiomatic modern code, directly supporting the PRD goal of providing a complete migration reference.

### Feature Completion Rule
This feature is considered **complete** when ALL of its User Stories have been delivered and their individual Definitions of Done have been met.

### User Stories

---
**Story ID:** F-001-US-01
**Title:** Implement age classification core logic

**User Story:**
> As a developer studying the reference, I want a pure function that takes an age (0-99) and returns the classification (ADULT / TEEN / CHILD) so that I can see how a conditional branch maps from COBOL to modern code.

**Functional Contribution:**
Establishes the core classification algorithm. Without this story, no age classification occurs regardless of interface.

**Definition of Ready (DoR)**
- [ ] Classification thresholds are agreed: ADULT >=18, TEEN >=13, CHILD <13
- [ ] Acceptance criteria are written and understood by the team
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given an age of 25, When classify() is called, Then it returns "ADULT"
- [ ] Given an age of 18, When classify() is called, Then it returns "ADULT"
- [ ] Given an age of 16, When classify() is called, Then it returns "TEEN"
- [ ] Given an age of 13, When classify() is called, Then it returns "TEEN"
- [ ] Given an age of 5, When classify() is called, Then it returns "CHILD"
- [ ] Given an age of 0, When classify() is called, Then it returns "CHILD"
- [ ] Code reviewed and merged
- [ ] Functional test scenarios for this story have passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Adult boundary — Age 18 returns "ADULT".
- **Scenario 2:** Teen boundary — Age 13 returns "TEEN".
- **Scenario 3:** Child boundary — Age 12 returns "CHILD".
- **Scenario 4:** Edge values — Age 0 returns "CHILD"; age 99 returns "ADULT".

---
**Story ID:** F-001-US-02
**Title:** CLI interface for age classification

**User Story:**
> As a user running the reference project, I want to invoke age classification from the command line so that I can test and observe the feature without modifying code.

**Functional Contribution:**
Wraps the core logic with a CLI entry point (argument parsing and output display). Without this story, the classification logic exists but cannot be exercised by a user.

**Definition of Ready (DoR)**
- [ ] F-001-US-01 is Done (core logic exists)
- [ ] CLI framework/CLI argument parsing library selected
- [ ] Acceptance criteria are written and understood by the team
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given the command is run with `--age 16`, When the program executes, Then it prints "TEEN" to stdout
- [ ] Given the command is run with `--age 100`, When the program executes, Then it prints an error message about invalid range
- [ ] Given the command is run with `--age -1`, When the program executes, Then it prints an error message about invalid range
- [ ] Given the command is run with `--age abc`, When the program executes, Then it prints an error message about non-numeric input
- [ ] Code reviewed and merged
- [ ] Functional test scenarios for this story have passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Valid input — `--age 16` prints "TEEN".
- **Scenario 2:** Out of range — `--age 100` prints error.
- **Scenario 3:** Non-numeric — `--age abc` prints error.

---

## Feature: Countdown

**Feature ID:** F-002
**PRD Reference:** REQ-002, REQ-018
**Priority:** Must Have

### Description
Accepts a starting integer N and counts down to 1, printing each step with a label. N is a parameter for MVP; the original COBOL hardcoded it to 3.

### Business Value
Demonstrates the migration of a PERFORM...UNTIL loop construct to a modern iterative pattern. Directly supports the PRD goal of providing comparative language semantics.

### Feature Completion Rule
This feature is considered **complete** when ALL of its User Stories have been delivered and their individual Definitions of Done have been met.

### User Stories

---
**Story ID:** F-002-US-01
**Title:** Implement countdown core logic

**User Story:**
> As a developer studying the reference, I want a function that generates a countdown sequence from N to 1 so that I can see how a loop construct maps from COBOL to modern code.

**Functional Contribution:**
Establishes the core countdown algorithm.

**Definition of Ready (DoR)**
- [ ] Output format agreed: "Counting down ... N" per step
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given N=3, When countdown() is called, Then it returns [3, 2, 1]
- [ ] Given N=1, When countdown() is called, Then it returns [1]
- [ ] Given N=0, When countdown() is called, Then it returns an empty list or error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Normal countdown — N=3 produces [3, 2, 1].
- **Scenario 2:** Single step — N=1 produces [1].
- **Scenario 3:** Zero or negative — N=0 or N=-1 produces error.

---
**Story ID:** F-002-US-02
**Title:** CLI interface for countdown

**User Story:**
> As a user running the reference project, I want to invoke the countdown from the command line so that I can test and observe the feature.

**Functional Contribution:**
Wraps the core logic with a CLI entry point.

**Definition of Ready (DoR)**
- [ ] F-002-US-01 is Done
- [ ] CLI framework selected (shared with F-001-US-02)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given the command is run with `--countdown 3`, When the program executes, Then it prints three lines: "Counting down ... 3", "Counting down ... 2", "Counting down ... 1"
- [ ] Given the command is run with `--countdown 1`, When the program executes, Then it prints one line: "Counting down ... 1"
- [ ] Given the command is run with `--countdown 0`, When the program executes, Then it prints an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Normal countdown — `--countdown 3` prints three lines.
- **Scenario 2:** Single step — `--countdown 1` prints one line.
- **Scenario 3:** Zero — `--countdown 0` prints error.

---

## Feature: Fibonacci Sequence Generator

**Feature ID:** F-003
**PRD Reference:** REQ-003, REQ-004, REQ-012
**Priority:** Must Have

### Description
Generates Fibonacci numbers F(1) through F(N) iteratively, with configurable start/end index filtering for display. Uses only integer arithmetic.

### Business Value
Demonstrates migration of a PERFORM VARYING loop with accumulator variables from COBOL to modern idiomatic code. The configurable range display improves on the original COBOL which hardcoded the skip threshold.

### Feature Completion Rule
This feature is considered **complete** when ALL of its User Stories have been delivered and their individual Definitions of Done have been met.

### User Stories

---
**Story ID:** F-003-US-01
**Title:** Implement Fibonacci generation core logic

**User Story:**
> As a developer studying the reference, I want a function that generates Fibonacci numbers F(1) through F(N) so that I can see how iterative computation with accumulator variables maps from COBOL to modern code.

**Functional Contribution:**
Establishes the core iterative Fibonacci algorithm.

**Definition of Ready (DoR)**
- [ ] Algorithm confirmed: iterative F(n) = F(n-1) + F(n-2) with F(0)=0, F(1)=1
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given N=10, When fibonacci() is called, Then it returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
- [ ] Given N=7, When fibonacci() is called, Then it returns [0, 1, 1, 2, 3, 5, 8]
- [ ] Given N=1, When fibonacci() is called, Then it returns [0]
- [ ] Given N=0, When fibonacci() is called, Then it returns [] or error
- [ ] Return type is integer-only (no floating point)
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Standard sequence — N=10 returns first 10 Fibonacci numbers.
- **Scenario 2:** Short sequence — N=1 returns [0].
- **Scenario 3:** Zero N — N=0 returns empty or error.

---
**Story ID:** F-003-US-02
**Title:** Configurable display range filtering

**User Story:**
> As a user running the reference, I want to display only a subset of the generated Fibonacci numbers by specifying a start and end index so that I can compare with the COBOL original's conditional output logic.

**Functional Contribution:**
Adds range-based display filtering, mirroring the COBOL original's WS-A_SKIP behaviour but with configurable bounds.

**Definition of Ready (DoR)**
- [ ] F-003-US-01 is Done
- [ ] Format agreed: "FIBONACCI [index] : [value]"
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given N=10 and range start=6, end=10, When display() is called, Then it returns ["FIBONACCI 6 : 5", "FIBONACCI 7 : 8", "FIBONACCI 8 : 13", "FIBONACCI 9 : 21", "FIBONACCI 10 : 34"]
- [ ] Given N=10 and range start=1, end=3, When display() is called, Then it returns ["FIBONACCI 1 : 0", "FIBONACCI 2 : 1", "FIBONACCI 3 : 1"]
- [ ] Given start > end, When display() is called, Then it returns an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Default COBOL-compatible range — N=10, range 6-10 matches original output.
- **Scenario 2:** Full range — N=5, range 1-5 displays all.
- **Scenario 3:** Invalid range — start > end returns error.

---
**Story ID:** F-003-US-03
**Title:** CLI interface for Fibonacci generation

**User Story:**
> As a user running the reference project, I want to invoke Fibonacci generation from the command line with configurable N and range so that I can test and observe the feature.

**Functional Contribution:**
Wraps the Fibonacci core and range filter with a CLI entry point.

**Definition of Ready (DoR)**
- [ ] F-003-US-01 and F-003-US-02 are Done
- [ ] CLI framework selected (shared)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given `--fibonacci 10 --range 6-10`, When the program executes, Then it prints "FIBONACCI 6 : 5" through "FIBONACCI 10 : 34"
- [ ] Given `--fibonacci 5`, When the program executes, Then it prints all 5 values
- [ ] Given `--fibonacci 0`, When the program executes, Then it prints an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** With range — `--fibonacci 10 --range 6-10` prints filtered output.
- **Scenario 2:** Without range — `--fibonacci 5` prints all values.
- **Scenario 3:** Zero — `--fibonacci 0` prints error.

---

## Feature: Interactive Two-Number Addition

**Feature ID:** F-004
**PRD Reference:** REQ-005, REQ-006, REQ-012, REQ-015
**Priority:** Must Have

### Description
Prompts the user for two integers (0-99 each), validates them, computes the sum, and displays the formatted result. Includes error handling for non-numeric and out-of-range input.

### Business Value
Demonstrates migration of ACCEPT/ADD/DISPLAY operations from COBOL to modern interactive I/O with input validation — the original COBOL had no validation, so this improves on the legacy code.

### Feature Completion Rule
This feature is considered **complete** when ALL of its User Stories have been delivered and their individual Definitions of Done have been met.

### User Stories

---
**Story ID:** F-004-US-01
**Title:** Implement addition core logic with input validation

**User Story:**
> As a developer studying the reference, I want a function that validates two integers (0-99 each) and returns their sum so that I can see how COBOL ADD maps to modern arithmetic with validation guards.

**Functional Contribution:**
Establishes the core addition and validation logic.

**Definition of Ready (DoR)**
- [ ] Input range agreed: 0-99 per operand
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given inputs 25 and 17, When add() is called, Then it returns 42
- [ ] Given inputs 0 and 0, When add() is called, Then it returns 0
- [ ] Given inputs 99 and 99, When add() is called, Then it returns 198
- [ ] Given input -1, When validate() is called, Then it returns an error
- [ ] Given input 100, When validate() is called, Then it returns an error
- [ ] Given non-numeric input, When validate() is called, Then it returns an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Valid sum — 25 + 17 = 42.
- **Scenario 2:** Boundary — 0 + 0 = 0; 99 + 99 = 198.
- **Scenario 3:** Out of range — negative or >99 returns error.

---
**Story ID:** F-004-US-02
**Title:** CLI interface for interactive addition

**User Story:**
> As a user running the reference project, I want to input two numbers interactively and see their sum displayed so that I can test and observe the feature.

**Functional Contribution:**
Wraps the addition core with interactive prompts and formatted output.

**Definition of Ready (DoR)**
- [ ] F-004-US-01 is Done
- [ ] CLI framework selected (shared)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given the command is run with `--add`, When the program executes, Then it prompts "INPUT Nr.1! Max is 99:", accepts input, prompts "INPUT Nr.2! Max is 99:", accepts input, and prints "RESULT: 25 + 17 = 42"
- [ ] Given non-numeric input at first prompt, When the user types "abc", Then it prints an error and re-prompts
- [ ] Given out-of-range input, When the user types "100", Then it prints an error and re-prompts
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Normal flow — Two valid inputs produce correct sum.
- **Scenario 2:** Non-numeric — "abc" triggers error and retry.
- **Scenario 3:** Out of range — "100" triggers error and retry.

---

## Feature: External Function Interop

**Feature ID:** F-005
**PRD Reference:** REQ-007, REQ-016
**Priority:** Should Have

### Description
Invokes an external function (system executable or script) by name with a numeric argument and captures its return value and output. Includes error handling for invocation failures.

### Business Value
Demonstrates how the COBOL CALL 'ctest' construct maps to modern inter-process or foreign-function invocation. Directly supports the PRD goal of providing a complete migration reference covering language interop.

### Feature Completion Rule
This feature is considered **complete** when ALL of its User Stories have been delivered and their individual Definitions of Done have been met.

### User Stories

---
**Story ID:** F-005-US-01
**Title:** Implement external function invocation mechanism

**User Story:**
> As a developer studying the reference, I want a function that invokes an external executable by name with a numeric argument and captures its exit code so that I can see how COBOL CALL maps to modern system invocation.

**Functional Contribution:**
Establishes the core invocation mechanism.

**Definition of Ready (DoR)**
- [ ] Mechanism agreed: invoke an external executable/script by name from system PATH (or explicit path)
- [ ] A stub external executable exists for testing
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given an external executable "ctest" exists that returns exit code 0 for argument 1337, When invoke("ctest", 1337) is called, Then it captures exit code 0 and stdout output
- [ ] Given an external executable that does not exist, When invoke() is called, Then it returns an error indicating "not found"
- [ ] Given an external executable that returns non-zero exit code, When invoke() is called, Then it captures the non-zero exit code
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Successful invocation — Existing executable with valid arg returns exit 0.
- **Scenario 2:** Not found — Non-existent executable returns error.
- **Scenario 3:** Non-zero exit — Executable returns exit 1, captured correctly.

---
**Story ID:** F-005-US-02
**Title:** CLI interface for external function invocation

**User Story:**
> As a user running the reference project, I want to invoke an external function from the command line so that I can test and observe the feature.

**Functional Contribution:**
Wraps the invocation mechanism with a CLI entry point.

**Definition of Ready (DoR)**
- [ ] F-005-US-01 is Done
- [ ] CLI framework selected (shared)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done (DoD)**
- [ ] Given the command is run with `--call ctest 1337`, When the program executes, Then it invokes ctest with argument 1337 and prints the exit code
- [ ] Given the command is run with `--call nonexistent 1`, When the program executes, Then it prints an error message
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**High-Level Test Scenarios**
- **Scenario 1:** Valid call — `--call ctest 1337` prints exit code.
- **Scenario 2:** Not found — `--call nonexistent 1` prints error.

## Out of Scope

| Item | Reason |
|------|--------|
| GUI or web interface | PRD specifies CLI-only for all features |
| Database persistence | Not present in the original COBOL; not in scope |
| Network/API layer | PRD explicitly out of scope |
| Real-time or concurrent behaviour | PRD explicitly out of scope |
| Production observability | Logging is informational only per PRD |
| Floating-point arithmetic | PRD REQ-012 mandates integer-only arithmetic |

## Handoff to Architecture

**Status:** Ready for architectural design

| Item | Value |
|------|-------|
| Feature count | 5 features, 11 user stories |
| Feature ID range | F-001 – F-005 |
| Open assumptions | ASS-001: External function mechanism deferred to IT Architect (system call / shared library / subprocess) |
| PRD reference | CobolDemoRefactored-1-Product-DOC-PRD-v1.0.md |

> To produce a Target Architecture Document (TAD) from this PFD, pass this document and the original PRD to the **it-architect** skill and say: **"Now analyse this PFD and produce an architecture."**
> Feature IDs in this document are stable traceability anchors — do not renumber them.
