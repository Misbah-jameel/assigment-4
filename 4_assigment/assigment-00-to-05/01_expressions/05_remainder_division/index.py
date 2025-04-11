def main():
    try:
        num1 = int(input("Please enter an integer to be divided: "))
        num2 = int(input("Please enter an integer to divide by: "))

        quotient = num1 // num2
        remainder = num1 % num2

        print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")
    except ValueError:
        print("Invalid input! Please enter valid integers.")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

if __name__ == "__main__":
    main()
