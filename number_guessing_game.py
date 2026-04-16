import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                return
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print(f"😢 Out of attempts! The number was {number}.")

def main():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y" , "YES", "Y" , "Yes"]:
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
