# CobolDemoRefactored — Stage 0 Orchestrator CONFIG: Tooling v1.0

**Project:** CobolDemoRefactored  
**Date:** 2026-06-03  
**Orchestrator:** SDLC Pipeline Agent (inline execution)

---

## Pre-Decided Tooling

| Concern | Tool | Notes |
|---------|------|-------|
| Task Management | GitHub Issues | Stories TF-001 to TF-005 tracked as Issues |
| Defect Management | GitHub Issues | Bug label applied to defect issues |
| CI/CD | GitHub Actions | Workflow added in Stage 5 (DevOps) |
| VCS | GitHub | Repo: https://github.com/frpinasco/CobolDemoRefactored |
| Language | Python 3.12 | Path: `C:\Program Files\Python314\python.exe` |
| Test Framework | pytest | With pytest-cov for coverage |
| Dependency Management | requirements.txt / requirements-dev.txt | stdlib + pytest only |

---

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable releases |
| `dev` | Integration branch for all feature work |
| `test` | QA / staging environment |
| `feature/TF-00N` | Per-story feature branches off `dev` |
| `chore/stage-N-*` | Per-stage artefact branches off `dev` |

---

## Execution Mode

Stages 0-4 executed inline by orchestrator agent (no sub-agent delegation).  
Rationale: task specification provides exact file layouts and code — specialist decisions pre-made.

---

## GitHub Repository

- **URL:** https://github.com/frpinasco/CobolDemoRefactored
- **Visibility:** Public
- **Default branch:** main
- **Remote:** origin
