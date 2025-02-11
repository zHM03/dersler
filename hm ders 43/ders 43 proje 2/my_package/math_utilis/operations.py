def divide(a, b):
    """Divides two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """Calculates the power of a number."""
    return a ** b
