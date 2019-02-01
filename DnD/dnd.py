#sabastian Taton
#Dungeons and dragons loot
#1-24-18

import random

def open_file():
    """ Opens the file"""
    try:
        item = open("loot_list.txt","r")
        spell = open("spell_list.txt","r")
        weapon = open("weapon_list.txt","r")
    except IOError as e:
        print("Unable to open file",file_name,"Ending program.",e)
        input("Press enter to exit the program.")
        sys.exit()
    else:
        return item, spell, weapon

def loot_choice(item, spell, weapon):
    type = [1,2,3]
    choice = random.choice(type)
    if choice == 1:
        loot = item.readlines()
        for i in range(4):
            itm = random.randrange(len(loot))
            print(loot[itm])
    if choice == 2:
        print("2")
        pass
    if choice == 3:
        print("3")
        pass
def main():
    item, spell, weapon = open_file()
    loot_choice(item, spell, weapon)

main()