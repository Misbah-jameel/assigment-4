
import random

def play():
    print("\n🪨 Rock - 📄 Paper - ✂ Scissors 🎮")
    print("-" * 40)

    user = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
    computer = random.choice(['r', 'p', 's'])

    choices = {'r': '🪨 Rock', 'p': '📄 Paper', 's': '✂ Scissors'}

    if user not in choices:
        return "❌ Invalid choice! Please select 'r', 'p', or 's'."

    print(f"\n🎮 You chose: {choices[user]}")
    print(f"🤖 Computer chose: {choices[computer]}")

    if user == computer:
        return "😲 It's a Tie!"

    if is_win(user, computer):
        return "🎉 You Won! 🏆"

    return "😞 You Lost! Try again!"

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

print(play())