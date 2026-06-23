# CobolDemoRefactored — Product Requirements Document (PRD)

**Document Version:** 1.0  
**Date:** June 24, 2026  
**Author:** Product Developer Agent  
**Status:** Draft — Stage 1 (Product)

---

## 1. Executive Summary

CobolDemoRefactored is a COBOL demonstration and testing utility (PROGRAM-ID: COBOL_TEST) that showcases core COBOL language features: data declarations, conditional branching, looping constructs, string manipulation, integer arithmetic, and C-language interoperability. It serves as both an educational reference for developers learning COBOL and a regression-test harness for COBOL compiler implementations. The program currently implements five features — age classification, countdown loop, Fibonacci sequence generation, interactive two-number addition, and an external C function call — all delivered as a single, self-contained COBOL source file.

---

## 2. Product Vision

**North star:** Become the canonical open-source reference program for validating COBOL compiler correctness and developer training across legacy-modernisation toolchains.

**5-year vision:** Every COBOL compiler, translator, and education platform ships with CobolDemoRefactored (or a derivative) as its standard "hello world of COBOL features" — the first program you compile when porting to a new platform, and the first lesson in every COBOL training course.

**Vision statement:** *A tiny, complete, portable COBOL program that exercises every essential language feature — from conditional logic to C interop — so developers and tools can validate correctness in under sixty seconds.*

---

## 3. Problem Statement (The Why)

**The problem:** COBOL remains critical in financial services, government, and insurance — yet there is no compact, well-documented, multi-feature reference program that can be used for compiler validation, developer training, and toolchain benchmarking. Most COBOL training materials are either outdated, vendor-specific, or exercise only a single feature in isolation.

**Who experiences it:**
- COBOL developers maintaining legacy systems need a quick smoke-test when porting code between environments
- Compiler and translator teams (e.g., COBOL-to-Java, COBOL-to-.NET) need a multi-feature regression suite
- Educators teaching COBOL in university or corporate training need a single worked example covering data, logic, loops, arithmetic, and interop

**Current solutions and their shortcomings:**
- Vendor sample programs (IBM, Micro Focus) are proprietary and platform-locked
- Open-source COBOL examples are fragmented across blogs and GitHub gists — no single authoritative reference exists
- Compiler test suites are internal, large, and not suitable for teaching

**Root cause:** No one has packaged a compact, multi-feature, portable COBOL program with a clear analysis document and a permissive licence.

---

## 4. The Solution (The What)

CobolDemoRefactored is a single COBOL source file (`main.cobol`) that performs five distinct demonstrations in sequence:

1. **Age classification** — Nested IF/ELSE conditional logic categorising a hardcoded age (16) as ADULT, TEEN, or CHILD
2. **Countdown loop** — PERFORM...UNTIL with AFTER test, counting 3 → 1 with manual decrement
3. **Fibonacci generation** — PERFORM VARYING loop computing F(1)–F(10) iteratively, displaying F(6)–F(10)
4. **Interactive addition** — ACCEPT two integers (0–99 each), ADD them, DISPLAY the result
5. **C function interop** — CALL to external `ctest` with argument 1337 (requires C object at link time)

**Out of scope:**
- Database access (no FILE-CONTROL or I-O sections)
- Floating-point arithmetic (all PIC 9(n) integer-only)
- File I/O or record processing
- Web/network interfaces
- Production-grade error handling (intentional scope — the program validates features, not robustness)

---

## 5. Target Audience

| Persona | Description | Need |
|---------|-------------|------|
| **COBOL Developer (Legacy Maintainer)** | 40+ year-old mainframe developers maintaining COBOL applications in banking/insurance | Quick smoke-test when porting between z/OS, GnuCOBOL, and cloud-emulated COBOL runtimes |
| **Compiler/Translator Engineer** | Engineers building COBOL front-ends, transpilers, or automated modernisation tooling | Multi-feature regression input to validate compiler correctness across data, control flow, arithmetic, and interop |
| **COBOL Student** | CS student or bootcamp attendee learning COBOL for mainframe modernisation projects | Single worked example that demonstrates all major language divisions and constructs |

Market segment: moderate — the COBOL developer community is small (~3–5 million active COBOL developers globally) but highly engaged and tool-dependent.

---

## 6. Market Analysis

### Competitive Landscape

| "Competitor" | Strengths | Weaknesses |
|-------------|-----------|------------|
| IBM Enterprise COBOL samples | Official, well-tested | Proprietary, platform-locked, no C interop example |
| GnuCOBOL test suite | Open-source, comprehensive | Large (1000+ files), no single entry point, no documentation |
| Micro Focus example programs | Professional quality | Vendor-locked, not portable to GnuCOBOL |
| Individual GitHub COBOL gists | Many small examples | Fragmented, inconsistent style, no analysis |

### Market Trends

- COBOL modernisation is accelerating (financial institutions migrating from mainframes to cloud)
- GnuCOBOL adoption is growing as a free, portable compiler
- AI-assisted COBOL translation (COBOL-to-Java, COBOL-to-C#, COBOL-to-Python) needs compact, well-analysed test inputs
- No single open-source "COBOL feature demo" has emerged as the standard — this gap is ripe

---

## 7. Competitive Moat

| Moat Type | Present? | Strength | How It Grows Over Time |
|-----------|----------|----------|------------------------|
| Network effects | No | N/A | Not applicable for a single-file demo program |
| Proprietary data | No | N/A | Code and analysis are open-source |
| Switching costs | No | N/A | Trivial to copy; moat is in community adoption, not technology |
| Brand / trust | Emerging | Weak | If adopted by COBOL toolchains as their standard demo, brand value grows |
| Regulatory licence | No | N/A | N/A |
| Exclusive partnerships | No | N/A | N/A |
| Technology / IP | No | N/A | No patentable technology |

**Summary verdict:** This product has no structural moat. Defensibility comes from first-mover adoption as the reference demo in COBOL tooling ecosystems, community contributions, and the accompanying analysis document (which has independent value).

---

## 8. Client Retention Analysis

| Retention Driver | Description | When It Kicks In |
|-----------------|-------------|-----------------|
| Compiler validation habit | Developers reach for CobolDemoRefactored first when testing a new COBOL environment | Immediate — it is the simplest way to validate a compiler works |
| Analysis document value | The reverse-engineering report provides structured insights no other COBOL demo has | On first read of the .md analysis |
| Curriculum embedding | University/bootcamp courses that adopt it as a teaching tool rarely switch | Semester 2+ |

**Churn risks:** The project is trivially forked. Community governance, responsiveness to issues, and CI/CD quality are the primary retention levers.

---

## 9. Monetisation Strategy

Not applicable — this is a free, open-source reference program. Value accrues indirectly through ecosystem adoption, which benefits the sponsoring organisation (e.g., a COBOL modernisation vendor) via brand awareness and toolchain compatibility.

---

## 10. Go-To-Market Plan

1. **Publish** the analysis report and PRD to GitHub
2. **Submit** to GnuCOBOL issue tracker as a suggested regression addition
3. **Promote** in COBOL communities: LinkedIn COBOL group, r/cobol on Reddit, SHARE conference
4. **Reach out** to COBOL modernisation vendors (Veryant, Heirloom, Evolveware) to adopt as a standard demo
5. **CI badge** in README showing compilation success on GnuCOBOL + IBM COBOL (via Hercules or similar)

---

## 11. Product Roadmap

| Phase | Goals | Key Features | Timeline |
|-------|-------|--------------|----------|
| MVP (current) | Single-file COBOL demo with analysis | F-001 through F-005 as analysed | Complete |
| V1 | Clean branch/tag per compiler target; add GnuCOBOL CI | GnuCOBOL pipeline, README, contributing guide | Q3 2026 |
| V2 | Expand feature set; add Python-equivalent reference | More COBOL features (STRING, INSPECT, table handling); reference .py files for each feature | Q1 2027 |
| V3 | ISAM file I/O demo | Add FILE-CONTROL, indexed file read/write, and a data-driven report | Q3 2027 |

---

## 12. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low community adoption | Medium | High | Proactive outreach to COBOL tool vendors and training organisations |
| Fork fragmentation | Medium | Low | Clear contribution governance, permissive licence, single-source-of-truth analysis document |
| Compiler divergence | Medium | Medium | CI matrix testing across GnuCOBOL, IBM COBOL, and Micro Focus |
| Analysis document becomes stale | Low | Medium | Automated regeneration pipeline (the analysis is generated by an agent, not hand-written) |

---

## 13. Regulatory & Compliance Considerations

None — the product is a feature-demonstration program with no data collection, no personal information processing, and no regulated-domain functionality.

---

## 14. Product Requirements Register

| REQ-ID | Category | Requirement | Priority (MoSCoW) | Source Section |
|--------|----------|-------------|-------------------|----------------|
| REQ-001 | FR | Classify age 0-99 into ADULT / TEEN / CHILD via nested IF/ELSE | Must Have | §4 – The Solution / F-001 |
| REQ-002 | FR | Display countdown from 3 to 1 using PERFORM...UNTIL with AFTER test | Must Have | §4 – The Solution / F-002 |
| REQ-003 | FR | Compute Fibonacci sequence positions 1-10 iteratively | Must Have | §4 – The Solution / F-003 |
| REQ-004 | FR | Display Fibonacci positions 6-10 with labels | Must Have | §4 – The Solution / F-003 |
| REQ-005 | FR | Accept two integer inputs (0-99) via ACCEPT | Must Have | §4 – The Solution / F-004 |
| REQ-006 | FR | Add two integers and display sum with labelled output | Must Have | §4 – The Solution / F-004 |
| REQ-007 | FR | CALL external C function `ctest` with integer argument 1337 | Should Have | §4 – The Solution / F-005 |
| REQ-008 | NFR | Integer-only arithmetic (no floating point, PIC 9(n) only) | Must Have | §8 – Constraints |
| REQ-009 | NFR | All output via DISPLAY to standard output (human-readable text) | Must Have | §4 – The Solution / F-004 |
| REQ-010 | NFR | No file I/O (no FILE-CONTROL or SELECT statements) | Must Have | §4 – Out of scope |
| REQ-011 | CON | Portable across COBOL compilers (GnuCOBOL, IBM, Micro Focus) | Should Have | §6 – Market Analysis |
| REQ-012 | CON | C interop requires external ctest.o / ctest.so at link time | Must Have | §4 – The Solution / F-005 |
| REQ-013 | ASS | The external `ctest` function accepts a single integer and returns void | Must Have | F-005 / Missing Information |
| REQ-014 | FR | Accept command-line or interactive input for user-driven values | Could Have | §9 – V1 Roadmap |
| REQ-015 | NFR | Error handling for non-numeric ACCEPT input | Should Have | §9 – Issue #1 Recommendation |
| REQ-016 | NFR | RETURN-CODE check after CALL 'ctest' | Should Have | §9 – Issue #3 Recommendation |

---

## 15. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Compiler support | 3 compilers (GnuCOBOL, IBM, Micro Focus) | CI pipeline passing on each |
| GitHub stars | 100+ within 12 months | GitHub analytics |
| Community contributions | 5+ external PRs within 12 months | GitHub pulse |
| Training adoption | 3+ training courses referencing it within 18 months | Manual tracking |
| Analysis document accuracy | 100% of agent-generated assertions verified by human review | Issue tracker |
