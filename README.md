# CobolDemoRefactored

Python 3.12 port of the COBOL_TEST demonstration program.

This project refactors a COBOL program into idiomatic Python 3.12, preserving all original features:

- **F-001** Age Group Classification
- **F-002** Countdown Loop (do-while semantics)
- **F-003** Fibonacci Sequence (positions 6-10)
- **F-004** Two-Integer Addition with input validation
- **F-005** External C Function stub (`ctest`)

## Quick Start

```bash
pip install -r requirements-dev.txt
python -m cobol_demo.main
pytest --cov=cobol_demo tests/
```

## Project Structure

```
src/cobol_demo/      # Application modules
tests/               # pytest unit tests
artifacts/           # SDLC artefacts (PRD, TAD, PFD, Backlog)
```
