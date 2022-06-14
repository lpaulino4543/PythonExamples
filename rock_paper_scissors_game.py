import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
      player = input("rock, paper, or scissors?:\n")
    if player == computer:
        print("Player:", player)
        print("Computer:", computer)
        print("It's a tie!, play again")
    elif player == "rock":
        if computer == "paper":
            print("Player:", player)
            print("Computer:", computer)
            print("You Lose!")
        if computer == "scissors":
            print("Player:", player)
            print("Computer:", computer)
            print("You Win!")
    elif player == "paper":
        if computer == "rock":
            print("Player:", player)
            print("Computer:", computer)
            print("You Win!")
        if computer == "scissors":
            print("Player:", player)
            print("Computer:", computer)
            print("You Lose!")
    elif player == "scissors":
        if computer == "rock":
            print("Player:", player)
            print("Computer:", computer)
            print("You Lose!")
        if computer == "paper":
            print("Player:", player)
            print("Computer:", computer)
            print("You Win!")

    play_again = input("Play again? (yes/no):")
    if play_again != "yes":
        break

print("Bye!")
