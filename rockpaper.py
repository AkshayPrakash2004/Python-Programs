import random
print("Welcome to rock paper and scissors!")
print("Choose rock-0 paper-1 or scissor-2")
choice=int(input())
cchoice=random.randint(0,2)
if cchoice == 0 and choice == 0:
    print("Computer chose Rock")
    print("Draw")
elif cchoice == 1 and choice == 1:
    print("Computer chose Paper")
    print("Draw")
elif cchoice == 2 and choice == 2:
    print("Computer chose Scissor")
    print("Draw")
elif cchoice == 1 and choice == 0:
    print("Computer chose Paper")
    print("Computer wins")
elif cchoice == 0 and choice == 1:
    print("Computer chose Rock")
    print("You win")
elif cchoice == 1 and choice == 2:
    print("Computer chose Paper")
    print("You wins")
elif cchoice == 2 and choice == 1:
    print("Computer chose Scissors")
    print("Computer win")
elif cchoice == 2 and choice == 0:
    print("Computer chose Scissors")
    print("You win")
elif cchoice == 0 and choice == 2:
    print("Computer chose Rock")
    print("Computer wins")