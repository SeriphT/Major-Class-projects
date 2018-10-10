import time

global Location
global Up
global Down
global Left
global Right
global Action

Action = "look, grab, get, smell, lick, smash, hit, turn, use" 
Up = "up, u, upwards, upward, north"
Down = "down, d, downwards, downward, south"
Left = "left, l, west, westward, w"
Right = "right, l, east, eastward, e"

def main():
   Intro()

def Intro():
    print("You awaken in a cave, no recollection of how you got there.")
    time.sleep(1)
    print("You look around finding a torch and a lighter.")
    time.sleep(1)
    print("You see a door to your left, sunlight leaking through the small slit it has.")
    time.sleep(1)
    print("You feel fear creeping upon you.")
    time.sleep(1)
    print("You must escape this place.")
    time.sleep(1)
    print("Now!")
    time.sleep(1)
    input("press Enter to continue")
    menu()

def menu():
    choice = "x"
    while choice == "x":
        choice = input("What will you do?").lower()
        if choice in Up or Down or Left or Right:
            Locate(choice)
        elif choice in Action:
            Action(choice)
        else:
            print("You find yourself blank minded. You quickly collect yourself again.")
            menu()

def Locate(choice):
    choice = choice
    if choice in Up:
        print(" ")
        
    elif choice in Down:
        print(" ")
    elif choice in Left:
        print(" ")
    elif choice in Right:
        print(" ")
    else:
        print("You made a wrong turn somewhere and find yourself back in the same room")
        menu()

def Action(choice):
    print("You used the right things to get here.")







main()
