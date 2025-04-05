import random

def number_guessing_game(lower=1,upper=10,max_tries=5):
   number = random.randint(lower,upper)
   attempts = 0

   #welcome message:
   print("\nWelcome To The Number Guessing Game:")
   print(f"\nYou have total {max_tries} chances to attempt\n")
   while attempts < max_tries:
        number_to_guess = input("Enter your guess:")
        if number_to_guess.isdigit():
            number_to_guess = int(number_to_guess)
            attempts +=1

            if (number_to_guess == number):
              print("Congratulations! You guess the right number...")
              print(f"You get correct guess in {attempts} attempts")
              print("You Won!")
              return
            elif number_to_guess < number:
              print("Hint: Try a Higher Number..")
            else :
             print("Hint: Try a Lower Number..")
            print(f"You have {max_tries-attempts} attempts left.Try Again...")
        else:
            print("Your guess must be an integer...")
   print(f"\nThe correct guess is {number}")
   print("You Lose!")
number_guessing_game() 