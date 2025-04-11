def get_first_element(lst):
    """Prints the first element of a non-empty list"""
    print("First element:", lst[0])

# Get user input to create the list
n = int(input("Enter the number of elements in the list: "))

user_list = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

# Call the function
get_first_element(user_list)
