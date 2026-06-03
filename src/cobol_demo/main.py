"""Main orchestrator — CobolDemoRefactored.

Runs all COBOL_TEST features in sequence, matching the original
COBOL program's execution flow:
  1. Display name (static)
  2. Classify age and display group
  3. Countdown loop (3 to 1)
  4. Fibonacci positions 6-10
  5. Interactive two-integer addition
  6. ctest stub call with argument 1337
"""

from cobol_demo.age_classifier import classify_age
from cobol_demo.countdown import display_countdown
from cobol_demo.fibonacci import display_fibonacci
from cobol_demo.addition import run_addition
from cobol_demo.ctest_stub import ctest


def main(age: int = 16) -> None:
    """Run all COBOL demo features in sequence.

    Args:
        age: Age value for classification (default 16, matching original COBOL).
    """
    # Static name display (matches COBOL WS-NAME = "x444556")
    name = "x444556"
    print(f"My name is : {name}")

    # F-001: Age Group Classification
    group = classify_age(age)
    print(f"My age is {age} and I am a(n) {group}")
    print()

    # F-002: Countdown Loop
    display_countdown(3)
    print()

    # F-003: Fibonacci Sequence (display positions 6-10)
    display_fibonacci(10, skip=5)
    print()

    # F-004: Two-Integer Addition with Validation
    run_addition()
    print()

    # F-005: ctest Stub
    ctest(1337)


if __name__ == "__main__":
    main()
