print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
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