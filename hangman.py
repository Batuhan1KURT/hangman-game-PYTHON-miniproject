import random
from words import words  # Import words from your module

def valid_word_selection():
    # Select a valid word from the list, excluding words with '-' or ' ' characters
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def print_hangman(wrong):
    # Display the hangman figure corresponding to the number of wrong guesses
    hangman_figures = [
        """
        +---+
            |
            |
            |
           ===
        """,
        """
        +---+
        O   |
            |
            |
           ===
        """,
        """
        +---+
        O   |
        |   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|   |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
            |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
       /    |
           ===
        """,
        """
        +---+
        O   |
       /|\\  |
       / \\  |
           ===
        """
    ]

    print(hangman_figures[wrong])

def word_print(word, guessed_letters):
    # Display the word with guessed letters filled in, and underscores for unguessed letters
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def hangman_game():
    # Select a word for the player to guess
    word_to_guess = valid_word_selection()
    guessed_letters = set()  # Keep track of guessed letters
    wrong_guesses = 0  # Count the number of incorrect guesses

    print("Welcome to Hangman!")
    word_print(word_to_guess, guessed_letters)  # Display the initial state of the word

    while wrong_guesses < 6:
        # Get a letter guess from the player
        guess = input("Guess a letter: ").upper().strip()

        # Check if the input is more than one letter
        while len(guess) > 1:
            print("Do not enter more than one letter!")
            wrong_guesses += 1
            print_hangman(wrong_guesses)
            guess = input("Guess a letter: ").upper().strip()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            print(f"You have guessed this letters so far: {guessed_letters}")
            continue

        guessed_letters.add(guess)  # Add the guessed letter to the set

        # Check if the guessed letter is not in the word
        if guess not in word_to_guess:
            wrong_guesses += 1
            print_hangman(wrong_guesses)

        word_print(word_to_guess, guessed_letters)  # Display the updated word

        # Check if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word_to_guess):
            print("Congratulations! You've guessed the word: ", word_to_guess)
            break

    # If the player runs out of attempts
    if wrong_guesses == 6:
        print("Sorry, you ran out of attempts. The word was: ", word_to_guess)

if __name__ == "__main__":
    hangman_game()
