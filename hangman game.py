import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
        else:
            print("Correct!")

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You guessed the word.")
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
