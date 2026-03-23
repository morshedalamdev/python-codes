import random

def print_welcome():
    """Print welcome message and game instructions"""
    print("=" * 60)
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯".center(60))
    print("=" * 60)
    print()
    print("📋 GAME DESCRIPTION:")
    print("   The computer picks a random number between 1 and 10.")
    print("   Your task is to guess what number it picked!")
    print("   You have unlimited attempts to find the correct number.")
    print()
    print("🎯 HOW TO PLAY:")
    print("   1. A random number between 1 and 10 is selected")
    print("   2. Enter your guess when prompted")
    print("   3. The game will tell you if your guess is:")
    print("      • Too low  (your number is smaller than the target)")
    print("      • Too high (your number is larger than the target)")
    print("      • Correct! (you've guessed the right number!)")
    print("   4. Keep guessing until you find the number")
    print()
    print("💡 TIPS:")
    print("   • Pay attention to the hints (too low/too high)")
    print("   • Use the feedback to narrow down your guesses")
    print("   • Start with numbers in the middle range")
    print()
    print("🏆 WINNING:")
    print("   Find the number to win! Good luck! 🍀")
    print()
    print("=" * 60)
    print()

def play_game():
    """Main game logic"""
    selected_num = random.randrange(1, 11)
    attempts = 0
    
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1
    
    while guess != selected_num:
        if guess < selected_num:
            print("❌ Too low! Try again.")
            guess = int(input("Enter another guess: "))
            attempts += 1
        elif guess > selected_num:
            print("❌ Too high! Try again.")
            guess = int(input("Enter another guess: "))
            attempts += 1
    
    print()
    print("🎉 Congratulations! You guessed the number! 🎉")
    print(f"The number was: {selected_num}")
    print(f"You took {attempts} attempt(s) to find it!")
    print()

# Print welcome message
print_welcome()

# Play the game
play_game()

# Ask if player wants to play again
while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        print()
        play_game()
    elif play_again == 'no' or play_again == 'n':
        print()
        print("Thanks for playing! Goodbye! 👋")
        break
    else:
        print("Please enter 'yes' or 'no'.")