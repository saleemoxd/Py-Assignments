import random

print("Welcome to Rock Paper Scissors!")

computer_score = 0
user_score = 0

def comp():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        choice = "R"
    elif computer_choice == 2:
        choice = "P"
    else:
        choice = "S"
    return choice

while True:
    user_choice = input("Enter your choice (R/P/S): ").upper()
    computer_choice = comp()

    print("Computer chooses:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != "Y":
        break

print("Thanks for playing!")


    