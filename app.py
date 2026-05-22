"""Simple utility functions - you'll add more!"""


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

def factorial (n: int) -> int:
    """Find the factorial fo a number n."""
    if n<0:
        raise ValueError("n is negative.")
    if n<=1:
        return 1
    
    return n*factorial(n-1)