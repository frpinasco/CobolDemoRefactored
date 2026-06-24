# CobolDemoRefactored — Features & Requirements

_Current stage: 2 — Features | Document version: 1.1 | Date: 2026-06-24 | Last enriched by: Functional Analyst_

## Product Summary

CobolDemoRefactored is a modern, technology-agnostic reimplementation of a legacy COBOL demonstration program. Five features reverse-engineered from COBOL analysis — age classification, countdown, Fibonacci generation, interactive addition, and external function interop — are rebuilt as a modular, testable, well-documented application in a modern language, serving as a legacy-to-modern migration reference.

## Requirements Register

| REQ-ID | Category | Requirement | Priority (MoSCoW) | Linked Feature(s) |
|--------|----------|-------------|-------------------|-------------------|
| REQ-001 | FR | Classify a numeric age (0-99) as ADULT (>=18), TEEN (>=13), or CHILD (<13) | Must Have | F-001 |
| REQ-002 | FR | Accept a starting integer N, count down to 1 with labelled output per step | Must Have | F-002 |
| REQ-003 | FR | Generate Fibonacci numbers F(1) through F(N) iteratively | Must Have | F-003 |
| REQ-004 | FR | Display Fibonacci results filtered by configurable start/end index range | Must Have | F-003 |
| REQ-005 | FR | Accept two integers via interactive input, validate range (0-99), and store | Must Have | F-004 |
| REQ-006 | FR | Compute the sum of two validated integers and display formatted result | Must Have | F-004 |
| REQ-007 | FR | Invoke an external/native function by name with a numeric argument and capture its return value | Should Have | F-005 |
| REQ-008 | NFR | All features are independently testable via unit tests | Must Have | — |
| REQ-009 | NFR | Each feature maps to a stable Feature ID traceable to the COBOL analysis | Must Have | F-001, F-002, F-003, F-004, F-005 |
| REQ-010 | NFR | CLI-only interface (no GUI) for all features | Must Have | — |
| REQ-011 | NFR | Modular architecture — each feature is its own module/class | Must Have | F-001, F-002, F-003, F-004, F-005 |
| REQ-012 | NFR | Integer arithmetic only (no floating point) for calculations | Must Have | F-003, F-004 |
| REQ-013 | CON | Build and run on at least one modern development platform | Must Have | — |
| REQ-014 | CON | Technology-agnostic design — no framework lock-in at the architecture level | Must Have | — |
| REQ-015 | NFR | Error handling for non-numeric or out-of-range interactive input | Should Have | F-004 |
| REQ-016 | NFR | Error handling for external function invocation failure | Should Have | F-005 |
| REQ-017 | FR | Configurable age classification thresholds (not hardcoded) | Could Have | F-001 |
| REQ-018 | FR | Accept starting value for countdown as a parameter (not hardcoded to 3) | Could Have | F-002 |

## Features

| Feature ID | Feature Name | Description | Priority (MoSCoW) | Phase | Source | Added By |
|------------|--------------|-------------|-------------------|-------|--------|----------|
| F-001 | Age Group Classification | Classify age 0-99 as ADULT (>=18), TEEN (>=13), or CHILD (<13) with configurable thresholds | Must Have | MVP | REQ-001, REQ-017 | Product Developer |
| F-002 | Countdown | Accept N, count down to 1 with labelled output per step | Must Have | MVP | REQ-002, REQ-018 | Product Developer |
| F-003 | Fibonacci Sequence Generator | Iteratively generate F(1)-F(N); display filtered by configurable index range | Must Have | MVP | REQ-003, REQ-004, REQ-012 | Product Developer |
| F-004 | Interactive Two-Number Addition | Accept two validated integers (0-99), compute sum, display formatted result | Must Have | MVP | REQ-005, REQ-006, REQ-012, REQ-015 | Product Developer |
| F-005 | External Function Interop | Invoke external function by name with numeric argument; handle return and errors | Should Have | MVP | REQ-007, REQ-016 | Product Developer |

## User Stories

_Last updated by: Functional Analyst | 2026-06-24_

---

### F-001 — Age Group Classification
**Priority:** Must Have | **PRD Reference:** REQ-001, REQ-017

**Feature Completion Rule:** Complete when ALL user stories below are Done.

#### F-001-US-01 — Implement age classification core logic
> As a developer studying the reference, I want a pure function that takes an age (0-99) and returns the classification (ADULT / TEEN / CHILD) so that I can see how a conditional branch maps from COBOL to modern code.

**Functional Contribution:** Establishes the core classification algorithm.

**Definition of Ready**
- [ ] Classification thresholds are agreed: ADULT >=18, TEEN >=13, CHILD <13
- [ ] Acceptance criteria are written and understood by the team
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given an age of 25, When classify() is called, Then it returns "ADULT"
- [ ] Given an age of 18, When classify() is called, Then it returns "ADULT"
- [ ] Given an age of 16, When classify() is called, Then it returns "TEEN"
- [ ] Given an age of 13, When classify() is called, Then it returns "TEEN"
- [ ] Given an age of 5, When classify() is called, Then it returns "CHILD"
- [ ] Given an age of 0, When classify() is called, Then it returns "CHILD"
- [ ] Code reviewed and merged
- [ ] Functional test scenarios for this story have passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Adult boundary — Age 18 returns "ADULT".
- **Scenario 2:** Teen boundary — Age 13 returns "TEEN".
- **Scenario 3:** Child boundary — Age 12 returns "CHILD".
- **Scenario 4:** Edge values — Age 0 returns "CHILD"; age 99 returns "ADULT".

---

#### F-001-US-02 — CLI interface for age classification
> As a user running the reference project, I want to invoke age classification from the command line so that I can test and observe the feature without modifying code.

**Functional Contribution:** Wraps the core logic with a CLI entry point.

**Definition of Ready**
- [ ] F-001-US-01 is Done (core logic exists)
- [ ] CLI framework selected
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given the command is run with `--age 16`, When the program executes, Then it prints "TEEN" to stdout
- [ ] Given the command is run with `--age 100`, When the program executes, Then it prints an error message about invalid range
- [ ] Given the command is run with `--age -1`, When the program executes, Then it prints an error message about invalid range
- [ ] Given the command is run with `--age abc`, When the program executes, Then it prints an error message about non-numeric input
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Valid input — `--age 16` prints "TEEN".
- **Scenario 2:** Out of range — `--age 100` prints error.
- **Scenario 3:** Non-numeric — `--age abc` prints error.

---

### F-002 — Countdown
**Priority:** Must Have | **PRD Reference:** REQ-002, REQ-018

**Feature Completion Rule:** Complete when ALL user stories below are Done.

#### F-002-US-01 — Implement countdown core logic
> As a developer studying the reference, I want a function that generates a countdown sequence from N to 1 so that I can see how a loop construct maps from COBOL to modern code.

**Functional Contribution:** Establishes the core countdown algorithm.

**Definition of Ready**
- [ ] Output format agreed: "Counting down ... N" per step
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given N=3, When countdown() is called, Then it returns [3, 2, 1]
- [ ] Given N=1, When countdown() is called, Then it returns [1]
- [ ] Given N=0, When countdown() is called, Then it returns an empty list or error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Normal countdown — N=3 produces [3, 2, 1].
- **Scenario 2:** Single step — N=1 produces [1].
- **Scenario 3:** Zero or negative — N=0 or N=-1 produces error.

---

#### F-002-US-02 — CLI interface for countdown
> As a user running the reference project, I want to invoke the countdown from the command line so that I can test and observe the feature.

**Functional Contribution:** Wraps the core logic with a CLI entry point.

**Definition of Ready**
- [ ] F-002-US-01 is Done
- [ ] CLI framework selected (shared with F-001-US-02)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given `--countdown 3`, When the program executes, Then it prints "Counting down ... 3", "Counting down ... 2", "Counting down ... 1"
- [ ] Given `--countdown 1`, When the program executes, Then it prints "Counting down ... 1"
- [ ] Given `--countdown 0`, When the program executes, Then it prints an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Normal — `--countdown 3` prints three lines.
- **Scenario 2:** Single — `--countdown 1` prints one line.
- **Scenario 3:** Zero — `--countdown 0` prints error.

---

### F-003 — Fibonacci Sequence Generator
**Priority:** Must Have | **PRD Reference:** REQ-003, REQ-004, REQ-012

**Feature Completion Rule:** Complete when ALL user stories below are Done.

#### F-003-US-01 — Implement Fibonacci generation core logic
> As a developer studying the reference, I want a function that generates Fibonacci numbers F(1) through F(N) so that I can see how iterative computation maps from COBOL to modern code.

**Functional Contribution:** Establishes the core iterative Fibonacci algorithm.

**Definition of Ready**
- [ ] Algorithm confirmed: iterative F(n) = F(n-1) + F(n-2) with F(0)=0, F(1)=1
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given N=10, When fibonacci() is called, Then it returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
- [ ] Given N=7, When fibonacci() is called, Then it returns [0, 1, 1, 2, 3, 5, 8]
- [ ] Given N=1, When fibonacci() is called, Then it returns [0]
- [ ] Given N=0, When fibonacci() is called, Then it returns [] or error
- [ ] Return type is integer-only (no floating point)
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Standard — N=10 returns first 10 Fibonacci numbers.
- **Scenario 2:** Short — N=1 returns [0].
- **Scenario 3:** Zero — N=0 returns empty or error.

---

#### F-003-US-02 — Configurable display range filtering
> As a user running the reference, I want to display only a subset of the generated Fibonacci numbers by specifying a start and end index so that I can compare with the COBOL original's conditional output logic.

**Functional Contribution:** Adds range-based display filtering.

**Definition of Ready**
- [ ] F-003-US-01 is Done
- [ ] Format agreed: "FIBONACCI [index] : [value]"
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given N=10 and range start=6, end=10, When display() is called, Then it returns ["FIBONACCI 6 : 5", ..., "FIBONACCI 10 : 34"]
- [ ] Given N=10 and range start=1, end=3, When display() is called, Then it returns ["FIBONACCI 1 : 0", "FIBONACCI 2 : 1", "FIBONACCI 3 : 1"]
- [ ] Given start > end, When display() is called, Then it returns an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Default COBOL-compatible range — N=10, range 6-10 matches original output.
- **Scenario 2:** Full range — N=5, range 1-5 displays all.
- **Scenario 3:** Invalid range — start > end returns error.

---

#### F-003-US-03 — CLI interface for Fibonacci generation
> As a user running the reference project, I want to invoke Fibonacci generation from the command line with configurable N and range so that I can test and observe the feature.

**Functional Contribution:** Wraps the Fibonacci core and range filter with a CLI entry point.

**Definition of Ready**
- [ ] F-003-US-01 and F-003-US-02 are Done
- [ ] CLI framework selected (shared)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given `--fibonacci 10 --range 6-10`, When the program executes, Then it prints "FIBONACCI 6 : 5" through "FIBONACCI 10 : 34"
- [ ] Given `--fibonacci 5`, When the program executes, Then it prints all 5 values
- [ ] Given `--fibonacci 0`, When the program executes, Then it prints an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** With range — `--fibonacci 10 --range 6-10` prints filtered output.
- **Scenario 2:** Without range — `--fibonacci 5` prints all values.
- **Scenario 3:** Zero — `--fibonacci 0` prints error.

---

### F-004 — Interactive Two-Number Addition
**Priority:** Must Have | **PRD Reference:** REQ-005, REQ-006, REQ-012, REQ-015

**Feature Completion Rule:** Complete when ALL user stories below are Done.

#### F-004-US-01 — Implement addition core logic with input validation
> As a developer studying the reference, I want a function that validates two integers (0-99 each) and returns their sum so that I can see how COBOL ADD maps to modern arithmetic with validation guards.

**Functional Contribution:** Establishes the core addition and validation logic.

**Definition of Ready**
- [ ] Input range agreed: 0-99 per operand
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given inputs 25 and 17, When add() is called, Then it returns 42
- [ ] Given inputs 0 and 0, When add() is called, Then it returns 0
- [ ] Given inputs 99 and 99, When add() is called, Then it returns 198
- [ ] Given input -1, When validate() is called, Then it returns an error
- [ ] Given input 100, When validate() is called, Then it returns an error
- [ ] Given non-numeric input, When validate() is called, Then it returns an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Valid sum — 25 + 17 = 42.
- **Scenario 2:** Boundary — 0 + 0 = 0; 99 + 99 = 198.
- **Scenario 3:** Out of range — negative or >99 returns error.

---

#### F-004-US-02 — CLI interface for interactive addition
> As a user running the reference project, I want to input two numbers interactively and see their sum displayed so that I can test and observe the feature.

**Functional Contribution:** Wraps the addition core with interactive prompts and formatted output.

**Definition of Ready**
- [ ] F-004-US-01 is Done
- [ ] CLI framework selected (shared)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given `--add`, When the program executes, Then it prompts, accepts input, and prints "RESULT: 25 + 17 = 42"
- [ ] Given non-numeric input, When the user types "abc", Then it prints an error and re-prompts
- [ ] Given out-of-range input, When the user types "100", Then it prints an error and re-prompts
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Normal flow — Two valid inputs produce correct sum.
- **Scenario 2:** Non-numeric — "abc" triggers error and retry.
- **Scenario 3:** Out of range — "100" triggers error and retry.

---

### F-005 — External Function Interop
**Priority:** Should Have | **PRD Reference:** REQ-007, REQ-016

**Feature Completion Rule:** Complete when ALL user stories below are Done.

#### F-005-US-01 — Implement external function invocation mechanism
> As a developer studying the reference, I want a function that invokes an external executable by name with a numeric argument and captures its exit code so that I can see how COBOL CALL maps to modern system invocation.

**Functional Contribution:** Establishes the core invocation mechanism.

**Definition of Ready**
- [ ] Mechanism agreed: invoke an external executable/script by name
- [ ] A stub external executable exists for testing
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given "ctest" exists and returns exit 0 for arg 1337, When invoke("ctest", 1337) is called, Then it captures exit code 0 and stdout
- [ ] Given a non-existent executable, When invoke() is called, Then it returns a "not found" error
- [ ] Given an executable that returns non-zero, When invoke() is called, Then it captures the non-zero exit code
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Successful invocation — Existing executable returns exit 0.
- **Scenario 2:** Not found — Non-existent executable returns error.
- **Scenario 3:** Non-zero exit — Executable returns exit 1, captured correctly.

---

#### F-005-US-02 — CLI interface for external function invocation
> As a user running the reference project, I want to invoke an external function from the command line so that I can test and observe the feature.

**Functional Contribution:** Wraps the invocation mechanism with a CLI entry point.

**Definition of Ready**
- [ ] F-005-US-01 is Done
- [ ] CLI framework selected (shared)
- [ ] Acceptance criteria are written and understood
- [ ] Story has been estimated

**Definition of Done**
- [ ] Given `--call ctest 1337`, When the program executes, Then it invokes ctest with arg 1337 and prints the exit code
- [ ] Given `--call nonexistent 1`, When the program executes, Then it prints an error
- [ ] Code reviewed and merged
- [ ] Functional test scenarios passed
- [ ] No open blocking defects

**Test Scenarios**
- **Scenario 1:** Valid call — `--call ctest 1337` prints exit code.
- **Scenario 2:** Not found — `--call nonexistent 1` prints error.

## Architectural / Technical Features

_Populated by the IT Architect and Senior Lead Developer._

## Traceability Notes

- REQ-IDs map directly to the Requirements Register in the full PRD (§14)
- Feature IDs (F-xxx) are stable anchors — do not renumber after creation
- Each F-xxx traces back to an equivalent COBOL feature in the analysis report (artifacts/main.cobol.ANALYSIS_REPORT.md)
- Story IDs (F-xxx-US-xx) are added by the Functional Analyst
- Technical story IDs (TS-xxx) are added by the Senior Lead Developer
- ADR/NFR IDs are added by the IT Architect
- Assumptions (ASS) must be validated before their linked features enter development
