import random
choices=["stone","paper","scissors"]

print("type quit to exit")



while True:
    comp=random.choice(choices)
    player=str(input("Choose Stone , Paper or Scissors ")).lower()
    if (player=="quit"):
        exit()
    if player !="Stone" and  player!="stone" and player!="paper" and player!="Paper" and player!="Scissors" and player!="scissors" and player!="about" and player!="About" and player!="ABOUT":
        print("invalid choice....Choose either stone, paper or scissors")
    if player=="stone" and comp=="paper":
        print("The computer chose: ",comp)
        print("computer won it took paper and caught your stone")
    elif player=="stone" and comp=="scissors":
        print("The computer chose: ",comp)
        print("Player won you broke the computer's scissors")
    elif player=="stone" and comp=="stone":
        print("The computer chose: ",comp)
        print("oh tie the player also chose stone and the same for the comp")
    elif player=="paper" and comp=="stone":
        print("The computer chose: ",comp)
        print("player won players paper caught the computer's stone")
    elif player=="paper" and comp=="paper":
        print("The computer chose: ",comp)
        print("tie as you both took paper")
    elif player=="paper" and comp=="scissors":
        print("The computer chose: ",comp)
        print("ooo the computer's scissors cut your paper")
    elif player=="scissors" and comp=="stone":
        print("The computer chose: ",comp)
        print("the computer's stone broke your scissor :(")
    elif player=="scissors" and comp=="paper":
        print("The computer chose: ",comp)
        print("hey u cut u won the computer took paper")
    elif player=="scissors" and comp=="scissors":
        print("The computer chose: ",comp)
        print("you both took scissors so tie")
    if player=="about" or player=="About" or player=="ABOUT":
        print("This game is created by Jaskamal Singla ")


    