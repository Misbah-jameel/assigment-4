import random

def high_low_game(num_rounds=5):
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    
    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}")
        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)
        
        print(f"Your number is {player_num}")
        
        while True:
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if guess in ['higher', 'lower']:
                break
            print("Please enter either higher or lower")
        
        correct = False
        if guess == 'higher' and player_num > computer_num:
            correct = True
        elif guess == 'lower' and player_num < computer_num:
            correct = True
        
        print(f"The computer's number was {computer_num}")
        
        if correct:
            score += 1
            print("You were right!", end=' ')
        else:
            print("Aww, that's incorrect.", end=' ')
        
        print(f"Your score is now {score}\n")
    
    print("\nThanks for playing!")
    
    # Conditional ending messages
    if score == num_rounds:
        print("Wow! You played perfectly!")
    elif score >= num_rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Play the game with 5 rounds
high_low_game(5)