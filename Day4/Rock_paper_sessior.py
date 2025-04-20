import ascii_art
import random

def game():
    ask = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n==>"))
    com_choose = random.randint(0,2)
    print("User Chooses")
    if ask == 0:
        print("Rock")
        print(ascii_art.rock())
    elif ask == 1:
        print("Paper")
        print(ascii_art.paper())
    elif ask == 2:
        print("Scissors")
        print(ascii_art.scissor())
    else:
        print("Wrong Choise")

    for i in range(3):
        print()
    
    print("System Chooses")
    if com_choose == 0:
        print("Rock")
        print(ascii_art.rock())
    elif com_choose == 1:
        print("Paper")
        print(ascii_art.paper())
    elif com_choose == 2:
        print("Scissors")
        print(ascii_art.scissor())
    else:
        print("Wrong Choise")
    
    return ask,com_choose

def winning_game(ask,com):
    if (ask == 0 and com == 2) or (ask == 1 and com == 0) or (ask == 2 and com == 1):
        print("!!!!!!!!!!!!!!!!!!!!User Wins!!!!!!!!!!!!!!!!!!!!!!!!")
    elif (ask == com):
        print("!!!!!!!!!!!!!!!!!!!!!!!Its a draw !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!Computer Wins!!!!!!!!!!!!!!!!!!!!!!!!")

x,y = game()
winning_game(x,y)


