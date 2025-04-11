def double(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = double(number)
    print("Double that is", result)

main()
