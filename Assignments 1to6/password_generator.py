import random
import string

print(""""
    Welcome to the Password Generator Program:  
      """
)


def password_generate(length=12):
    characters = string.ascii_letters + string.octdigits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Users input

length = int(input("Enter your password length:"))

password = password_generate(length)

print("Your Password is:" , password)