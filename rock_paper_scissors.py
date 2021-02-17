import random

print("Welcome to rock paper scissors, play q to quit the game..")
legal_moves = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

while True:
    user_move = input("What do you play? ").lower()

    if user_move == 'q':
        break

    if user_move in legal_moves:
        computer_move = random.choice(legal_moves)

        if user_move == "rock" and computer_move == "rock":
            print(f"Computer plays {computer_move}")
            print("Draw")
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "rock" and computer_move == "paper":
            print(f"Computer plays {computer_move}")
            print("Computer wins")
            computer_score += 1
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "rock" and computer_move == "scissors":
            print(f"Computer plays {computer_move}")
            print("Player wins")
            player_score += 1
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "paper" and computer_move == "rock":
            print(f"Computer plays {computer_move}")
            print("Player wins")
            player_score += 1
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "paper" and computer_move == "paper":
            print(f"Computer plays {computer_move}")
            print("Draw")
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "paper" and computer_move == "scissors":
            print(f"Computer plays {computer_move}")
            print("Computer wins")
            computer_score += 1
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "scissors" and computer_move == "rock":
            print(f"Computer plays {computer_move}")
            print("Computer wins")
            computer_score += 1
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "scissors" and computer_move == "paper":
            print(f"Computer plays {computer_move}")
            print("Player wins")
            player_score += 1
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

        elif user_move == "scissors" and computer_move == "scissors":
            print(f"Computer plays {computer_move}")
            print("Draw")
            print(f"Player score: {player_score}")
            print(f"Compute score: {computer_score}")

    else:
        print('That is not a legal move')
        print("Please enter either rock, paper or scissors")
