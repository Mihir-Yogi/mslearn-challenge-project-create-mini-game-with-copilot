#create a simple minigame in python that game name is rock paper scissors.
#the winner of the game is determined by three simple rules: Rock beats scissors, Scissors beat paper, Paper beats rock.
#Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
#now create game as specified above.
import random
import os
def game():
    print("Welcome to Rock, Paper, Scissors Game")
    player_score = 0
    computer_score = 0
    while True:
        player = input("Enter Rock, Paper, or Scissors: ").lower()
        computer = random.choice(["rock", "paper", "scissors"])
        if player not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please enter Rock, Paper, or Scissors.")
            continue
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "paper":
            if computer == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "scissors":
            if computer == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        print(f"Player Score: {player_score}")
        print(f"Computer Score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
        os.system('cls' if os.name == 'nt' else 'clear')
game()


#Output:
#Welcome to Rock, Paper, Scissors Game
#Enter Rock, Paper, or Scissors: rock
#Player: rock
#Computer: rock
#It's a tie!
#Player Score: 0
#Computer Score: 0
#Do you want to play again? (yes/no): yes

