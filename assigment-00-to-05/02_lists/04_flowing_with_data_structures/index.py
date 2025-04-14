def add_three_copies(lst, data):
    """Adds three copies of the data to the list"""
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Empty list
my_list = []

# Get user input
message = input("Enter a message to copy: ")

print("List before:", my_list)

# Function call (modifies the original list)
add_three_copies(my_list, message)

print("List after:", my_list)
