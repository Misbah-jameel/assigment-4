import random
import string
import pyfiglet

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def display_banner():
    banner = pyfiglet.figlet_format("Password Generator")
    print(f"\033[1;34m{banner}\033[0m")

def main():
    display_banner()
    print("\033[1;32mGenerating an 8-character password...\033[0m")
    password = generate_password()
    print(f"\n\033[1;32mGenerated Password: {password}\033[0m")
    print("\033[1;33mKeep it safe! 🔐\033[0m")

main()