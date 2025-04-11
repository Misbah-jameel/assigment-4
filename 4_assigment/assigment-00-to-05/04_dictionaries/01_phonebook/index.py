def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break  # Stop if the user presses Enter without a name
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break  # Exit the loop if user presses Enter without a name
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}: {phonebook[name]}")


def main():
    phonebook = read_phone_numbers()  # Read phone numbers
    print_phonebook(phonebook)  # Print the phonebook
    lookup_numbers(phonebook)  # Look up phone numbers


if __name__ == '__main__':
    main()
