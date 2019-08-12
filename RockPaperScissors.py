# Two player (Rock Paper Scissor) game
"""
    print("Rock..")
    print("paper..")
    print("scissors..")

    player1=input("player-1, make your move:  " )
    player2=input("player-2, make your move:  ")

    if player1=="rock" and player2=="scissors":
        print("player1 wins!!")
    elif player1=="rock" and player2=="paper":
        print("player2 wins!!")
    elif player1=="paper" and player2=="rock":
        print("player1 wins!!")
    elif player1=="paper" and player2=="scissors":
        print("player2 wins!!")
    elif player1=="scissors" and player2=="paper":
        print("player1 wins!!")
    elif player1==player2:
        print("it's a tie!!")
    else:
        print("Something went wrong")


""" 

# Rock Paper Scissors Game with computer

from random import randint
player_wins=0
computer_wins=0
winning_score=3

while player_wins<winning_score and computer_wins<winning_score:
    print(f"Player Score: {player_wins}   Computer Score : {computer_wins}"  )
    

    player=input("Make your move: ").lower()
    if player=="quit" or player=="q":
        break
    random_number=randint(0,2)
    if(random_number==0):
        computer="rock"
    elif(random_number==1):
        computer="paper"
    else:
        computer="scissors"

    print(f"The computer's turn: {computer}")
    if player==computer:
        print("It's a tie!")
    elif player == "rock":
        if computer=="paper":
            print("Computer Wins..")
            computer_wins+=1
        else:
            print("Player Wins!")
            player_wins+=1
    elif player=="paper":
        if computer=="rock":
            print("Player Wins!!")
            player_wins+=1
        else:
            print("Computer Wins..")
            computer_wins+=1
    elif player=="scissors":
        if computer=="rock":
            print("Computer Wins..")
            computer_wins+=1
        else:
            print("Player Wins!!")
            player_wins+=1
    else:
        print("Please enter a Valid String")

if player_wins>computer_wins:
    print("Congrats , You Won")
elif player_wins==computer_wins:
    print("It's a Tie!!")
else:
    print("Oh, No You lost and Computer Won!!")