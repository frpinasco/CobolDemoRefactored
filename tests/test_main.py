"""Unit tests for main orchestrator — integration coverage."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobol_demo.main import main


def test_main_runs_all_features(monkeypatch, capsys) -> None:
    """main() runs all 5 COBOL features in sequence with expected output."""
    # Provide inputs for the interactive addition prompt (F-004)
    inputs = iter(["25", "17"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main(age=16)

    captured = capsys.readouterr()

    # F-001: name and age group
    assert "My name is : x444556" in captured.out
    assert "My age is 16 and I am a(n) TEEN" in captured.out

    # F-002: countdown
    assert "Counting down ... 3" in captured.out
    assert "Counting down ... 2" in captured.out
    assert "Counting down ... 1" in captured.out

    # F-003: fibonacci
    assert "FIBONACCI 6 : 5" in captured.out
    assert "FIBONACCI 7 : 8" in captured.out
    assert "FIBONACCI 10 : 34" in captured.out

    # F-004: addition result
    assert "RESULT: 25 + 17 = 42" in captured.out

    # F-005: ctest stub
    assert "ctest called with: 1337" in captured.out


def test_main_with_adult_age(monkeypatch, capsys) -> None:
    """main() correctly classifies an adult age."""
    inputs = iter(["10", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main(age=25)

    captured = capsys.readouterr()
    assert "My age is 25 and I am a(n) ADULT" in captured.out
