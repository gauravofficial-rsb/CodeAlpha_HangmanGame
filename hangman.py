import random

# List of predefined words
words = ["python", "computer", "programming", "hangman", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
attempts_left = max_attempts

print(" Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while attempts_left > 0:
    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts Left:", attempts_left)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or incorrect guess
    if guess not in word:
        attempts_left -= 1
        print("❌ Wrong guess!")

# Game Over
if attempts_left == 0:
    print("\n Game Over!")
    print("The correct word was:", word)