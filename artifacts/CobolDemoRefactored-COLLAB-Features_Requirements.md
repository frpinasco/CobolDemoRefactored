# CobolDemoRefactored — Features & Requirements

_Current stage: 1 — Product | Document version: 1.0 | Date: 2026-06-24 | Last enriched by: Product Developer_

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

_Populated by the Functional Analyst._

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
