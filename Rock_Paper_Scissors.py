import random
game=["rock","paper","scissors"]

player_score=0
computer_score=0
rounds=0

while True:
    rounds+=1
    print("\nround:",rounds)

    computer=random.choice(game)
    player=input("Enter rock,paper,scissors:").lower()
    if player not in game:
        print("invalid choice!! Try again.")
        rounds+=1
        continue
    print("computer turn",computer)
    print("you turn",player)
    if player == computer:
        print("Tie")

    elif(player=="rock" and computer=="scissors")or\
        (player=="paper" and computer=="rock")or\
        (player=="scissors"and computer=="paper"):
        print("you win!!")
        player_score+=1
    else:
        print("you lose!!")
        computer_score+=1
    print("score=you:",player_score,"|computer:",computer_score)
    if rounds==3:
        print("\nfinal result")
        if player_score > computer_score:
            print("overall winner")
        elif computer_score > player_score:
            print("computer won")
        else:
            print("it is a tie")
        play_again=input("play again?(yes/no:").lower()
        if play_again!="yes":
           print("Thanks for playing")
           break
        else:
         if play_again=="yes":
            rounds=0
            player_score=0
            computer_score=0
            print("\nStarting new game..\n")
            continue