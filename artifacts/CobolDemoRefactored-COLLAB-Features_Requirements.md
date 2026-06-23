# CobolDemoRefactored — Features & Requirements

_Current stage: 1 — Product | Document version: 1.0 | Date: 2026-06-24 | Last enriched by: Product Developer_

## Product Summary

CobolDemoRefactored is a single-file COBOL demonstration program (PROGRAM-ID: COBOL_TEST) that validates core COBOL language features — data declarations, conditional logic, loops, integer arithmetic, string display, and C-language interop — for compiler validation, developer training, and toolchain benchmarking.

## Requirements Register

| REQ-ID | Category | Requirement | Priority (MoSCoW) | Linked Feature(s) |
|--------|----------|-------------|-------------------|-------------------|
| REQ-001 | FR | Classify age 0-99 into ADULT / TEEN / CHILD via nested IF/ELSE | Must Have | F-001 |
| REQ-002 | FR | Display countdown from 3 to 1 using PERFORM...UNTIL with AFTER test | Must Have | F-002 |
| REQ-003 | FR | Compute Fibonacci sequence positions 1-10 iteratively | Must Have | F-003 |
| REQ-004 | FR | Display Fibonacci positions 6-10 with labels | Must Have | F-003 |
| REQ-005 | FR | Accept two integer inputs (0-99) via ACCEPT | Must Have | F-004 |
| REQ-006 | FR | Add two integers and display sum with labelled output | Must Have | F-004 |
| REQ-007 | FR | CALL external C function `ctest` with integer argument 1337 | Should Have | F-005 |
| REQ-008 | NFR | Integer-only arithmetic (no floating point, PIC 9(n) only) | Must Have | F-001, F-003, F-004 |
| REQ-009 | NFR | All output via DISPLAY to standard output (human-readable text) | Must Have | F-001, F-002, F-003, F-004 |
| REQ-010 | NFR | No file I/O (no FILE-CONTROL or SELECT statements) | Must Have | — |
| REQ-011 | CON | Portable across COBOL compilers (GnuCOBOL, IBM, Micro Focus) | Should Have | F-001, F-002, F-003, F-004, F-005 |
| REQ-012 | CON | C interop requires external ctest.o / ctest.so at link time | Must Have | F-005 |
| REQ-013 | ASS | The external `ctest` function accepts a single integer and returns void | Must Have | F-005 |
| REQ-014 | FR | Accept command-line or interactive input for user-driven values | Could Have | F-001 |
| REQ-015 | NFR | Error handling for non-numeric ACCEPT input | Should Have | F-004 |
| REQ-016 | NFR | RETURN-CODE check after CALL 'ctest' | Should Have | F-005 |

## Features

| Feature ID | Feature Name | Description | Priority (MoSCoW) | Phase | Source | Added By |
|------------|--------------|-------------|-------------------|-------|--------|----------|
| F-001 | Age Group Classification | Nested IF/ELSE classifying age 0-99 as ADULT (>=18), TEEN (>=13), or CHILD (<13) | Must Have | MVP | REQ-001 | Product Developer |
| F-002 | Countdown Loop | PERFORM...UNTIL countdown from 3 to 1 with manual counter decrement via SUBTRACT | Must Have | MVP | REQ-002 | Product Developer |
| F-003 | Fibonacci Sequence Generator | Iterative computation of F(1)-F(10) using PERFORM VARYING with conditional display of positions 6-10 | Must Have | MVP | REQ-003, REQ-004 | Product Developer |
| F-004 | Interactive Two-Number Addition | ACCEPT two integers (0-99), ADD them, DISPLAY result with labelled output | Must Have | MVP | REQ-005, REQ-006 | Product Developer |
| F-005 | External C Function Interop | CALL to external C function `ctest` with integer argument 1337 | Should Have | MVP | REQ-007, REQ-012, REQ-013 | Product Developer |

## User Stories

_Populated by the Functional Analyst._

## Architectural / Technical Features

_Populated by the IT Architect and Senior Lead Developer._

## Traceability Notes

- REQ-IDs map directly to the Requirements Register in the full PRD (§14)
- Feature IDs (F-xxx) are stable anchors — do not renumber after creation
- Story IDs (F-xxx-US-xx) are added by the Functional Analyst
- Technical story IDs (TS-xxx) are added by the Senior Lead Developer
- ADR/NFR IDs are added by the IT Architect
- Assumptions (ASS) must be validated before their linked features enter development
