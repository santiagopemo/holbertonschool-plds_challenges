#!/usr/bin/python3
from base_champion import BaseChampion
from fighter import Fighter
from cleric import Cleric
from mage import Mage
from ranger import Ranger
from paladin import Paladin
from rogue import Rogue
import fighter
from os import path
import random


champ_types = [Cleric, Fighter, Mage, Paladin, Ranger, Rogue]

def create_champion():
        print("==============================")
        print("    Select your champion      ")
        print("1-Cleric   2-Figther  3-Mage  ")
        print("4-Paladin  5-Ranger   6-Rouge ")
        print("*Any other option to go back  ")
        try:
            op2 = int(input(">> "))
            if not 0 < op2 < 7:
                raise Exception
        except:
            return None
        while 1:
            try:
                c_name = input("Enter champions name\n>> ")
                c_raze = input("Enter champions raze\n>> ")
                c_gender = input("Enter champions gender\n>> ")
            except:
                print("Error, try again")
                continue
            my_champ = champ_types[op2 - 1](c_name, c_raze, c_gender, 0, 5, 0, 0, 0)
            print(my_champ)
            return my_champ

def upgrade_champion(my_champ):
    print("====== Upgrade Champion ======")
    print("Stats Points: {}".format(my_champ.stats_points))
    print("what do you want to upgrade?")
    print("*Any other option to go back")
    for key, value in my_champ.stats.items():
        print("{}: {} ".format(key, value), end="")
        print()
    while 1:
        try:
            op_uc = input(">> ")
            if my_champ.stats.get(op_uc, False) == 0:
                raise Exception
            print("how much?")
            quantitie = int(input(">> "))
            if quantitie < 0 or quantitie > my_champ.stats_points:
                raise ValueError
            else:
                my_champ.stats[op_uc] += quantitie
                print("Upgraded {} to {}".format(op_uc, my_champ.stats[op_uc]))
                return 1
        except ValueError:
            print("Wrong quantitie")
            return 0
        except:
            print("Error, try again")
            return 0

def load_champion():
    print("Enter Champions Type")
    ch_type = input(">> ")
    print("Enter Champions name")
    ch_name = input(">> ")
    ch_dict = BaseChampion.load_character(ch_type, ch_name)
    if ch_dict == {}:
        print("no champion found")
        return None
    if ch_type == "Cleric":
        my_champ = Cleric(ch_dict["name"], ch_dict["raze"], ch_dict["gender"], ch_dict["level"], ch_dict["nv_exp"], ch_dict["current_exp"], ch_dict["total_exp"], ch_dict["stat_points"])
    if ch_type == "Paladin":
        my_champ = Paladin(ch_dict["name"], ch_dict["raze"], ch_dict["gender"], ch_dict["level"], ch_dict["nv_exp"], ch_dict["current_exp"], ch_dict["total_exp"], ch_dict["stat_points"])
    if ch_type == "Figther":
        my_champ = Figther(ch_dict["name"], ch_dict["raze"], ch_dict["gender"], ch_dict["level"], ch_dict["nv_exp"], ch_dict["current_exp"], ch_dict["total_exp"], ch_dict["stat_points"])
    if ch_type == "Mage":
        my_champ = Mage(ch_dict["name"], ch_dict["raze"], ch_dict["gender"], ch_dict["level"], ch_dict["nv_exp"], ch_dict["current_exp"], ch_dict["total_exp"], ch_dict["stat_points"])
    if ch_type == "Rogue":
        my_champ = Rogue(ch_dict["name"], ch_dict["raze"], ch_dict["gender"], ch_dict["level"], ch_dict["nv_exp"], ch_dict["current_exp"], ch_dict["total_exp"], ch_dict["stat_points"])
    if ch_type == "Ranger":
        my_champ = Ranger(ch_dict["name"], ch_dict["raze"], ch_dict["gender"], ch_dict["level"], ch_dict["nv_exp"], ch_dict["current_exp"], ch_dict["total_exp"], ch_dict["stat_points"])
    my_champ.stats = ch_dict["stats"]
    print(my_champ)
    return my_champ


def fight(my_champ):
    ty = random.randint(0, 5)
    enemy = champ_types[ty]("Enemy", "Bug", "Bug", 0, 5, 0, 0, 0)
    print("Your Enemy is")
    print(enemy)
    my_damage = 0
    enemy_damage = 0
    print("===============BEGIN!!!=======================")
    while 1:
        print("{} {} healt: {}".format(type(enemy).__name__,enemy.name,enemy.stats["health"]))
        print("{} {} healt: {}".format(type(my_champ).__name__,my_champ.name,my_champ.stats["health"]))
        print("1-Attack     2-Use magic")
        try:
            f_op = int(input(">> "))
            if f_op != 1 and f_op != 2:
                raise Exception
        except:
            break
        enemy_damage = enemy.defend() - my_champ.attack()
        if enemy_damage < 0:
            enemy.stats["health"] += enemy_damage
        my_damage = my_champ.defend() - enemy.attack()
        if my_damage < 0:
            my_champ.stats["health"] += my_damage

# player1 = Cleric()
# print("Player1 upload")
# f1 = Fighter("Javier", "Programmer", "male", 10, 5, 0, 20, 4)
# c1 = Cleric("Javier", "Programmer", "male", 10, 5, 0, 20, 4)
# r1 = Ranger("Javier", "Programmer", "male", 10, 5, 0, 20, 4)
# fs1 = fighter.Solar("Javier", "Programmer", "male", 10, 5, 0, 20, 4)
# f1.increase_stats({"health": 100, "attack": 100, "defense": 100, "magic": 100, "speed": 100})
# fs1.save_character()
# print("\n================ level 1 :::::: JAVIER IS PLAYING IN THE GAME =============\n")
# print(BaseChampion.load_character("Cleric", "Javier"))    
# c1.increase_stats({"health": 100, "attack": 100, "defense": 100, "magic": 100, "speed": 100})
# c1.save_character()
# print("\n================ level 2 :::::: JAVIER IS PLAYING IN THE GAME =============\n")
# print(c1.load_character())
# print("\n================ level 2 :::::: JAVIER IS CHOOSE SKILLS' ATACK =============\n")
# print(int(fs1.attack()))
# print(int(fs1.defend()))
# print(int(fs1.use_magic()))


while 1:
    print("===========================")
    print("    THE HOLBIE CHAMPION    ")
    print("===========================")
    print("1-Create a new champion")
    print("2-Load a existing champion")
    print("*Any other option to exit")
    try:
        op1 = int(input(">> "))
        if op1 != 1 and op1 != 2:
            raise Exception
    except:
        break
        print()
    if op1 == 1:
        my_champ = create_champion()
        if my_champ == None:
            continue            
    if op1 == 2:
        my_champ = load_champion()
        if my_champ == None:
            continue
    while 1:
        print("1-New fight  2-Upgrade Champion  3-Save Champion")
        print("*Any other option to go back")
        try:
            op4 =int(input(">> "))
            if not 0 < op4 < 4:
                raise Exception
        except:
            break
            print()
        if op4 == 1:
            fight(my_champ)
        if op4 == 2:
            upgrade_champion(my_champ)

        if op4 == 3:
            my_champ.save_character()
            print("Champion Saved")
    print()

print()


        
