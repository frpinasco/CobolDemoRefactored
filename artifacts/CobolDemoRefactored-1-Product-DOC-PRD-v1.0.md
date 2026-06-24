# CobolDemoRefactored — Product Requirements Document (PRD)

**Document Version:** 1.0  
**Date:** June 24, 2026  
**Author:** Product Developer Agent  
**Status:** Draft — Stage 1 (Product)

---

## 1. Executive Summary

CobolDemoRefactored is a modern, technology-agnostic reimplementation of a legacy COBOL demonstration program. A functional reverse-engineering analysis of the original COBOL source identified five core features — age group classification, iterative countdown, Fibonacci sequence generation, interactive two-number addition, and external function interoperability — that will be rebuilt as a clean, modular, well-tested application in a modern language. The project serves dual purposes: as a reference example for developers learning modern software construction patterns, and as an evidence-based case study in legacy-to-modern migration, where every design decision is traced back to the original COBOL analysis.

---

## 2. Product Vision

**North star:** Become the canonical reference example for legacy-to-modern migration — a small, complete, well-documented case study showing how to take a reverse-engineered legacy program and rebuild it with modern language idioms, modular architecture, and automated testing.

**5-year vision:** Developers and teams evaluating legacy modernisation start here. The repository is the first link shared when someone asks "How do I approach migrating a COBOL program to a modern stack?"

**Vision statement:** *A tiny, complete, technology-agnostic rebuild of a legacy COBOL program — from analysis to deployment — demonstrating how every legacy feature maps to a modern, testable, modular counterpart.*

---

## 3. Problem Statement (The Why)

**The problem:** Organisations running COBOL mainframes face mounting pressure to modernise (skill shortages, cloud migration, regulatory compliance), but there is no small, end-to-end reference project that demonstrates the full migration lifecycle — from reverse-engineering a legacy program to shipping a modern equivalent. Every migration project starts from scratch, repeating the same patterns and learnings.

**Who experiences it:**
- **Technical leads** evaluating legacy-modernisation tooling and approaches need a proof-of-concept they can complete in a day, not a month
- **Developers new to COBOL modernisation** need a worked example they can study end-to-end
- **Vendors of modernisation tooling** need a standard benchmark program to validate their output

**Current solutions and their shortcomings:**
- Migration case studies are typically high-level PowerPoint decks, not working code
- Open-source COBOL-to-X translators exist but are tool-specific and hard to evaluate without a reference input/output pair
- No standard "before and after" program exists for comparing modernisation approaches

**Root cause:** No one has packaged both the legacy analysis and the modern rebuild into a single, traceable, open-source reference project.

---

## 4. The Solution (The What)

CobolDemoRefactored takes the five features extracted from the COBOL analysis and rebuilds them in a modern language with:

1. **Age Classification (F-001)** — Given a numeric age (0-99), classify as ADULT (>=18), TEEN (>=13), or CHILD (<13) with configurable thresholds
2. **Countdown (F-002)** — Accept a starting integer N, count down to 1 with labelled output per step, then terminate
3. **Fibonacci Sequence (F-003)** — Generate F(1) through F(N) iteratively, with optional display filtering by index range
4. **Interactive Addition (F-004)** — Accept two integers (validated within range), compute sum, display formatted result
5. **External Function Interop (F-005)** — Invoke an external/native function by name with a numeric argument and handle its return value and errors

Every feature is: modular (own module/class), testable (unit tests), independently runnable, and traced back to the original COBOL analysis via feature IDs.

**Out of scope:**
- No graphical user interface (CLI-only)
- No persistence layer or database
- No network or web API
- No real-time or concurrent behaviour
- No production-grade observability — logging is informational

---

## 5. Target Audience

| Persona | Description | Need |
|---------|-------------|------|
| **Modernisation Technical Lead** | Architect evaluating legacy-migration strategy for their organisation | A complete, small-scale reference they can fork, run, and extend |
| **Developer (Legacy Modernisation)** | Software engineer tasked with migrating a specific COBOL program | A worked example showing how each COBOL construct maps to modern code |
| **Tooling Evaluator** | Engineer comparing COBOL-to-X translators | A standard "expected output" to validate tool correctness |

---

## 6. Market Analysis

### Competitive Landscape

| "Competitor" | Strengths | Weaknesses |
|-------------|-----------|------------|
| IBM COBOL-to-Java translator demos | Official from vendor | Proprietary, Java-only, no standalone analysis document |
| GnuCOBOL test suite (compiler tests) | Comprehensive, open-source | Focused on compiler correctness, not migration patterns |
| Blog posts / conference talks (e.g., SHARE) | Good narrative | No code, no traceability back to source |
| Academic papers on COBOL migration | Deep analysis | No executable deliverables; hard to evaluate |

### Market Trends

- COBOL modernisation market is growing (Gartner: legacy modernisation spending increasing 12% YoY)
- Cloud providers (AWS DMS, Azure Carbon) are adding COBOL migration services — they need reference inputs
- AI-assisted code conversion (LLM-based) is rising but lacks standard evaluation benchmarks
- No single open-source "legacy → modern" before-and-after reference exists

---

## 7. Competitive Moat

| Moat Type | Present? | Strength | How It Grows Over Time |
|-----------|----------|----------|------------------------|
| Network effects | No | N/A | Not applicable for a reference project |
| Proprietary data | Yes (analysis) | Weak | The COBOL analysis document is co-generated by an agent; increasing the feature set grows its utility |
| Switching costs | Low | Weak | Trivially forkable; moat is in community recognition, not technology |
| Brand / trust | Emerging | Weak | If adopted as a teaching tool by modernisation courses, brand value grows |
| Technology / IP | No | N/A | All content is open-source |

**Summary verdict:** No structural moat. Defensibility comes from being the first and most complete "before + after" reference, community contributions, and the traceability chain linking every modern feature back to the legacy analysis.

---

## 8. Client Retention Analysis

| Retention Driver | Description | When It Kicks In |
|-----------------|-------------|-----------------|
| Fork-and-run reference | Developer forks, runs the project, modifies it for their own migration — they keep coming back for updates | After first successful use |
| Feature traceability | No other project links a COBOL analysis report to modern code line-by-line via stable IDs | On first comparison |
| Curriculum embedding | University courses adopt it as a "legacy modernisation lab" exercise | Semester 2+ |

**Churn risks:** Staleness (if the COBOL analysis is not kept in sync with the code); competition from vendor-specific demos.

---

## 9. Monetisation Strategy

Not applicable — this is an open-source reference project. Value accrues indirectly via ecosystem adoption, toolchain compatibility, and organisational brand awareness for the sponsor.

---

## 10. Go-To-Market Plan

1. **Publish** analysis report + PRD + code + tests as a complete GitHub repository
2. **Submit** to relevant GitHub topic lists: `cobol`, `legacy-modernisation`, `migration-reference`
3. **Promote** in COBOL modernisation communities (Reddit r/cobol, LinkedIn COBOL Modernisation group, SHARE conference)
4. **Outreach** to COBOL tooling vendors (Veryant, Heirloom, Evolveware) and cloud COBOL migration services
5. **README CI badge** showing build + test passing on the modern implementation

---

## 11. Product Roadmap

| Phase | Goals | Key Features | Timeline |
|-------|-------|--------------|----------|
| MVP | All 5 features implemented, tested, and traced to COBOL analysis | F-001 through F-005 with unit tests | Q3 2026 |
| V1 | CI pipeline, README, contribution guide, Docker support | Full dev experience, multi-platform | Q3 2026 |
| V2 | Add additional COBOL features (STRING, INSPECT, tables, file I/O) | Enriched feature set, comparative benchmarks | Q1 2027 |
| V3 | ISAM file I/O demo in modern equivalent | Data-driven feature with persistence | Q3 2027 |

---

## 12. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low adoption | Medium | High | Proactive outreach to modernisation community and tool vendors |
| Analysis-code drift | Medium | Medium | Feature IDs in analysis are stable anchors; code modules reference them |
| Language choice limits audience | Medium | Medium | The PRD is language-agnostic — the actual language choice is an implementation detail for Stage 3 (Architecture) |
| Incomplete reverse engineering | Low | Medium | Analysis covers all code paths in the original program; cross-referenced line-by-line |

---

## 13. Regulatory & Compliance Considerations

None — the product is a feature-demonstration project with no data collection, PII processing, or regulated-domain functionality.

---

## 14. Product Requirements Register

| REQ-ID | Category | Requirement | Priority (MoSCoW) | Source Section |
|--------|----------|-------------|-------------------|----------------|
| REQ-001 | FR | Classify a numeric age (0-99) as ADULT (>=18), TEEN (>=13), or CHILD (<13) | Must Have | §4 – The Solution / F-001 |
| REQ-002 | FR | Accept a starting integer N, count down to 1 with labelled output per step | Must Have | §4 – The Solution / F-002 |
| REQ-003 | FR | Generate Fibonacci numbers F(1) through F(N) iteratively | Must Have | §4 – The Solution / F-003 |
| REQ-004 | FR | Display Fibonacci results filtered by configurable start/end index range | Must Have | §4 – The Solution / F-003 |
| REQ-005 | FR | Accept two integers via interactive input, validate range (0-99), and store | Must Have | §4 – The Solution / F-004 |
| REQ-006 | FR | Compute the sum of two validated integers and display formatted result | Must Have | §4 – The Solution / F-004 |
| REQ-007 | FR | Invoke an external/native function by name with a numeric argument and capture its return value | Should Have | §4 – The Solution / F-005 |
| REQ-008 | NFR | All features are independently testable via unit tests | Must Have | §9 – Definition of quality |
| REQ-009 | NFR | Each feature maps to a stable Feature ID traceable to the COBOL analysis | Must Have | §9 – Traceability |
| REQ-010 | NFR | CLI-only interface (no GUI) for all features | Must Have | §4 – Out of scope |
| REQ-011 | NFR | Modular architecture — each feature is its own module/class | Must Have | §4 – The Solution |
| REQ-012 | NFR | Integer arithmetic only (no floating point) for calculations | Must Have | REQ-003, REQ-006 |
| REQ-013 | CON | Build and run on at least one modern development platform (Linux, macOS, Windows) | Must Have | §4 – Out of scope |
| REQ-014 | CON | Technology-agnostic design — no framework lock-in at the architecture level | Must Have | §4 – The Solution |
| REQ-015 | NFR | Error handling for non-numeric or out-of-range interactive input | Should Have | F-004 |
| REQ-016 | NFR | Error handling for external function invocation failure | Should Have | F-005 |
| REQ-017 | FR | Configurable age classification thresholds (not hardcoded) | Could Have | F-001 |
| REQ-018 | FR | Accept starting value for countdown as a parameter (not hardcoded to 3) | Could Have | F-002 |

---

## 15. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Build + test | 100% green on CI | CI pipeline status |
| Unit test coverage | >80% per module | Coverage report |
| Feature traceability | 5/5 features traced to COBOL analysis IDs | COLLAB document review |
| GitHub stars | 100+ within 12 months | GitHub analytics |
| External contributions | 5+ PRs within 12 months | GitHub pulse |
