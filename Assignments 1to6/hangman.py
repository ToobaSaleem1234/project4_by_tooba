import random

# List of programming words
programming_words = [ 
    "algorithm", "variable", "function", "loop", "array", "class", "object", "debugging",
    "compiler", "syntax", "module", "method", "condition", "recursion", "pointer", "data",
    "binary", "hashmap", "string", "constant", "framework", "inheritance", "polymorphism",
    "closure", "exception", "parameter", "stack", "queue", "interface", "algorithmic",
    "iteration", "database", "network", "thread", "concurrency", "asynchronous", "scripting",
    "html", "css", "javaScript", "python", "ruby", "java", "c++", "php", "sql"
]

# Choose a random word
random_generate = random.choice(programming_words)
guessed_words = ["_"] * len(random_generate)
attempts = 5 
guessed_letters = []

# Introduction
print("\nWelcome to the Hangman Game!\n")
print("Guess the word by letter...\n")
print(f"The word has {len(random_generate)} letters... and you have {attempts} chances to guess...\n")

# Game loop
while attempts > 0:
    # Display the current progress
    print("\nWord:", " ".join(guessed_words))
    print(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    print(f"Remaining attempts: {attempts}")

    # User Input
    guess = input("\nEnter your guess letter: ").lower()

    # Input Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input! Please enter a single letter.\n")
        continue

    # Check if the letter is already guessed
    if guess in guessed_letters:
        print("You already guessed this letter! Try another letter.\n")
        continue

    # Add the guess to guessed letters list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the random word
    if guess in random_generate:
        print(f"Correct guess! '{guess}' is in the word.")
        # Replace blanks with the correct guessed letter
        for i in range(len(random_generate)):
            if random_generate[i] == guess:
                guessed_words[i] = guess
    else:
        print(f"Oops! Wrong guess! '{guess}' is not in the word. Try Again.")
        attempts -= 1

    # Check if the word is fully guessed
    if "_" not in guessed_words:
        print(f"\nCongratulations! You guessed the correct word: {random_generate}")
        break

# If the user runs out of attempts
if attempts == 0:
    print("\nGame Over! You ran out of attempts.")
    print(f"The correct word was: {random_generate}")