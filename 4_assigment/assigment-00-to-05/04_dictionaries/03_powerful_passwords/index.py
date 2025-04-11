# Assuming hash_password is provided and works as a hash function to hash passwords
def hash_password(password: str) -> str:
    # This function should return a hashed password
    pass  # This will be defined externally

# This dictionary holds the email and its corresponding password hash
stored_logins = {
    "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",  # Example hashed password
}

def login(email: str, password_to_check: str) -> bool:
    # Check if the email exists in the stored_logins dictionary
    if email in stored_logins:
        # Hash the entered password
        hashed_password = hash_password(password_to_check)
        # Compare the hashed entered password with the stored hash
        return hashed_password == stored_logins[email]
    else:
        # Email not found in the system
        return False

# Example usage
email = "user@example.com"
password = "hello"  # Example password to check

if login(email, password):
    print("Login successful!")
else:
    print("Login failed!")
