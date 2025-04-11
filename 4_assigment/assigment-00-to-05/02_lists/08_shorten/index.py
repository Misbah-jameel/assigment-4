MAX_LENGTH = 3  # Set the maximum allowed length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Keep removing until the list is MAX_LENGTH
        removed_item = lst.pop()  # Remove the last element
        print("Removed:", removed_item)  # Print the removed element

def main():
    lst = input("Enter list elements separated by spaces: ").split()  # Get user input as a list
    print("Original List:", lst)
    shorten(lst)  # Call shorten function
    print("Final List:", lst)  # Print the shortened list

# Run the program
main()
