def feet_to_inches(feet):
    """Convert feet to inches"""
    return feet * 12

def main():
    try:
        feet = float(input("Enter length in feet: "))
        inches = feet_to_inches(feet)
        print(f"{feet} feet is equal to {inches} inches.")
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()

