import random

print("""
      Welcome to the Number Guessing Game (User):
""")
print("Guess the Number between 1 - 100")

def number_guess_user(lower=1, upper=100, max_tries=10):
    number = random.randint(lower, upper)
    attempts = 0

    while attempts < max_tries:
        # Handle invalid input
        try:
            guess = int(input("Enter your Guess Number:"))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1

        if guess > number:
            print("Hint: Try a Lower Number...")
        elif guess < number:
            print("Hint: Try a Higher Number...")
        else:
            print("Congratulations! You guessed the Correct Number..")
            print("You Won!")
            return
        
        print(f"You have {max_tries - attempts} attempts left. Try Again...\n")
    
    print(f"The correct number was: {number}")
    print("You LOSE")

number_guess_user()
