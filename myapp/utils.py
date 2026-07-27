def is_even(n: int) -> bool:
    return n % 2 == 0

def greet(name: str) -> str:
    if not name:
        return "Hello guest"
    return f"Hello {name}"
