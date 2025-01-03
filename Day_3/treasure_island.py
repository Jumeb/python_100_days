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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('You are standing at the crossroads where the adventure begins. Do you want to go "Right" or "Left" \n')
if direction.lower() == 'left':
    action = input('You are faced by a seemingly beautiful breathing taking lake. Are you going to "Swim" or "Wait" for a boat?\n')
    if action.lower() == 'wait':
        door = input('Three doors, one option, which do you choose "Red", "Green" or "Yellow" \n')
        if door.lower() == 'red':
            print('Sorry, you met Medusa, the cursed princess and you turned to stone')
        elif door.lower() == 'blue':
            print('You ran out of luck, you entered the house of theives and thugs and you were killed')
        elif door.lower() == 'yellow':
            print('You are the champion and you were blesses with tons of gold and diamonds')
        else:
            print('That door doesn\'t exist. Game over')
    else:
      print('Oh nooo, you were close but the cursed lake crocodiles got to you')    
else:
    print("You were met by thieves and thugs and they killed you.")
    