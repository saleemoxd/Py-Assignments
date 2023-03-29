import random

print("Welcome to the random password generator!")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*)("
numbers = "0123456789"

all_chars = upper + lower + symbols + numbers

while True:
    length = int(input("How many characters would you like your password to be? "))
    password = "".join(random.sample(all_chars, length))
    print("Your new password is:", password)

    choice = input("Would you like to generate another password? (y/n): ")
    if choice.lower() != 'y':
        print("Thank you for using the password generator!")
        break
