def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

# Example usage:
print("Check 1:")
print("Is 5 in range 1 to 10? ", in_range(5, 1, 10))   # True

print("\nCheck 2:")
print("Is 0 in range 1 to 10? ", in_range(0, 1, 10))   # False

print("\nCheck 3:")
print("Is 10 in range 1 to 10? ", in_range(10, 1, 10)) # True

print("\nCheck 4:")
print("Is 1 in range 1 to 10? ", in_range(1, 1, 10))   # True
