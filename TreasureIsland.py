print("Welcome to treasure Island, where your decision will decide if you are getting treasure or not.")
left_or_right=input("where you wanna go? 'left' or 'right'? \n")

if left_or_right == 'left':
    print("You have chosen the RIGHT path. This will led you to treasure!!!")
    swim_or_wait=input("Do you wanna swim or wait?\n ")
    if swim_or_wait == 'wait':
        print("Fortunately you waited for the boat to cross the river, and reached shore safely!")
        door=input("Which door you wanna enter? 'red','yellow' or 'blue' : \n")
        if door=='blue':
            print("Eaten by beasts.\nGame over.")
        elif door=='red':
            print("Burned by fire.\nGame over.")
        elif door=='yellow':
            print("You Win!!The treasure is all yours.")
        else:
            print("game over.")
    else:
        print("Attacked by trout.\nGame over.")
else:
    print("you fell into a hole.\nGame over.")    