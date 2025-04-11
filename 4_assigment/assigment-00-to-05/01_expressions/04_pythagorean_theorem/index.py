import math

def calculate_hypotenuse(a, b):
    """Calculate the hypotenuse using Pythagorean theorem"""
    return math.sqrt(a**2 + b**2)

def main():
    try:
        a = float(input("Enter the length of AB: "))
        b = float(input("Enter the length of AC: "))
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"\nThe length of BC (the hypotenuse) is: {hypotenuse}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
