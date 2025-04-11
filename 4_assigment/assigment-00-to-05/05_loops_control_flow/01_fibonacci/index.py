# Define the maximum value for Fibonacci terms
MAX_VALUE = 10000

def fibonacci_sequence():
    # Initializing the first two Fibonacci numbers
    a, b = 0, 1
    
    # Print the first Fibonacci number (0)
    print(a, end=" ")

    # Continue to generate Fibonacci numbers until they exceed MAX_VALUE
    while b <= MAX_VALUE:
        print(b, end=" ")
        a, b = b, a + b  # Update a and b to the next two Fibonacci numbers

# Call the function to print the Fibonacci sequence
fibonacci_sequence()
