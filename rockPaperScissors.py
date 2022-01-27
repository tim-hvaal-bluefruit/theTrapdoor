# keep track of wins
# check user input against list of answers
# if in list that't the users choice
# choose a random number based on the list an assign to comp_choice

import random

options = ['rock', 'paper', 'scissors']
player_wins = 0
comp_wins = 0

while True:
  player_choice = input("do you choose rock, paper or scissors... or q to quit? \n")
  if player_choice == 'q': #get results only when you quit
    if comp_wins < player_wins:
      print(f"you played well squire - you won with {player_wins} wins! The wretched computer only won {comp_wins}" + "\n")
    elif comp_wins == player_wins:
      print(f"twas a draw, {player_wins} a piece, fair play", "\n")
    else:
      print(f"that wretched computer beat you - {comp_wins} to {player_wins}", "\n")
    break

  elif player_choice not in options:
    continue

  #computer choice
  rand = random.randrange(0, len(options))
  comp_choice = options[rand]

  #compare the two ... seems to be the most efficient way to do it
  if player_choice == comp_choice:
    print("you both chose", player_choice, "... draw", "\n")
    continue

  elif player_choice == 'rock' and comp_choice == 'scissors':
    print('comp chose scissors, you won!', "\n")
    player_wins += 1

  elif player_choice == 'paper' and comp_choice == 'rock':
    print('comp chose rock, you won!', "\n")
    player_wins += 1

  elif player_choice == 'scissors' and comp_choice == 'paper':
    print('comp chose paper, you won!', "\n")
    player_wins += 1
  
  else:
    print(f'computer chose {comp_choice} you lost :(', "\n")
    comp_wins += 1
