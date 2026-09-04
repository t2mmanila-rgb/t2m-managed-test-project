"""Math Utilities Module — T2M Managed Project"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers. Added by Agent 1."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divides a by b. Added by Agent 2."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
