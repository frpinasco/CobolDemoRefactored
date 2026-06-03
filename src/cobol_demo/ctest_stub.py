"""External C Function Stub — F-005.

Python stub replacing the COBOL: CALL 'ctest' using 1337

The original COBOL program called an external C function 'ctest' with
numeric argument 1337. In the Python port, this is a pure Python stub
that prints a confirmation message, removing the C runtime dependency.
"""


def ctest(value: int) -> None:
    """Stub for the external C function 'ctest'.

    Prints a confirmation message indicating the function was called
    with the given value. Replaces COBOL: CALL 'ctest' using 1337

    Args:
        value: The integer argument passed to ctest (original: 1337).
    """
    print(f"ctest called with: {value}")
