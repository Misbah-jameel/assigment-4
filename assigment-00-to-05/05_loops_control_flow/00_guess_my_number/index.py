import random

def guess_my_number():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    while True:
        # Ask the user to enter a guess
        guess = int(input("Enter a guess: "))
        
        # Check if the guess is too high, too low, or correct
        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break  # Exit the loop when the guess is correct

# Call the function to start the game
guess_my_number()
