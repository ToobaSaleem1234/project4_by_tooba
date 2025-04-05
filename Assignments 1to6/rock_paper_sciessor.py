import random
# welcome message:
print("\nWelcome To ROCK PAPER SCIESSOR GAME\n")
user_choice = input("Enter your choice: Press 'r' for Rock, 'p' for Paper, 's' for Sciessor...")

# function for game:
def rock_paper_sciessor():
 if user_choice not in ['r', 'p', 's']:
    print("Enter a valid input here.....")
 else:
    random_choice = random.choice(['r', 'p', 's'])
    print(f"Computer Chose:{random_choice}")

    if user_choice == 'r' and random_choice == 'p':
        print('You Lose...!')
    elif user_choice == 'r' and random_choice == 's':
        print("You Won...!")
    elif user_choice == 'p' and random_choice == 'r':
        print("You Won...!")
    elif user_choice == 'p' and random_choice == 's':
        print("You Lose...!")
    elif user_choice == 's' and random_choice == 'r':
        print("You Lose...!")
    elif user_choice == 's' and random_choice == 'p':
        print("You Won...!")
    else :
        print("Game Draw...!")
rock_paper_sciessor()
