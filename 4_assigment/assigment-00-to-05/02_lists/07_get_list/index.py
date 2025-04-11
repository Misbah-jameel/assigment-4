def main():
    values = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":  # Stop when user presses enter without input
            break
        values.append(user_input)  # Add value to list
    
    print("Here's the list:", values)

# Run the program
main()
