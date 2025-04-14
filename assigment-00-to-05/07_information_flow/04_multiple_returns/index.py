def get_user_info():
    # User se data lena
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")
    
    # Teeno cheezein return karna (tuple form mein)
    return first_name, last_name, email_address

########## Yahaan se neeche kuch change nahi karna :) ##########

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
