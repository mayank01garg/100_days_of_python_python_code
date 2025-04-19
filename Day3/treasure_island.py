from art import art
print(art())
for i in range(6):
    print()


print("Welcome to Treasure Island.\nYour mission is to find the treasure")
ask1 = input("left or right? ")
if ask1 == 'left':
    ask2 = input("swim or wait? ")
    if ask2 == 'wait':
        ask3 = input("Which door Red, Blue, Yellow?? ")
        if ask3 == 'Red':
            print("Burned by fire\nGame Over.")
        elif ask3 == 'Yellow':
            print("You Win!")
        elif ask3 == 'Blue':
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")