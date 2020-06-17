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
import os
import time
import glob


champ_types = [Cleric, Fighter, Mage, Paladin, Ranger, Rogue]

def create_champion():
        print("====== Create Champion ======")
        print("  Select your champions type ")
        print("1-Cleric   2-Figther  3-Mage ")
        print("4-Paladin  5-Ranger   6-Rouge")
        print("*Any other option to go back ")
        try:
            op2 = int(input(">> "))
            if not 0 < op2 < 7:
                raise Exception
        except:
            return None
        while 1:
            try:
                os.system("clear")
                print("====== Create Champion ======")
                c_name = input("Enter champions name\n>> ")
                os.system("clear")
                print("====== Create Champion ======")
                c_raze = input("Enter champions raze\n>> ")
                os.system("clear")
                print("====== Create Champion ======")
                c_gender = input("Enter champions gender\n>> ")
            except:
                os.system("clear")
                print("\nError, try again\n")
                input("Press enter to continue")
                continue
            my_champ = champ_types[op2 - 1](c_name, c_raze, c_gender, 0, 5, 0, 0, 2)
            os.system("clear")
            print("Your champion:")
            print(my_champ)
            input("Press enter to continue")
            return my_champ

def upgrade_champion(my_champ):
    print("===== Upgrade Champion =====")
    print("Stats Points: {}".format(my_champ.stats_points))
    print("what do you want to upgrade?")
    print("*Any other option to go back")
    print(28 * "=")
    for key, value in my_champ.stats.items():
        print("{:<10} {:>16} ".format(key, value), end="")
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
                my_champ.stats_points -= quantitie
                os.system("clear")
                print("\nUpgraded {} to {}\n".format(op_uc, my_champ.stats[op_uc]))
                input("Press enter to continue")
                return 1
        except ValueError:
            os.system("clear")
            print("\nWrong quantitie\n")
            input("Press enter to continue")
            return 0
        except:
            # os.system("clear")
            # print("Error, try again")
            # input("Press enter to continue")
            return 0

def load_champion():
    # print("Enter Champions Type")
    # ch_type = input(">> ")
    # print("Enter Champions name")
    # ch_name = input(">> ")
    jsonfiles = []
    for f in glob.glob("*.json"):
        jsonfiles.append(f)
    if jsonfiles == []:
        print("\nNo champions saved\n")
        input("Press enter to continue")
        return None
    print("===== Load Champion =====")
    for i, n in enumerate(jsonfiles):
        print("{}-{}".format(i + 1, n[:-5]))
    try:
        print("*Any other option to go back")
        l_op = int(input(">> "))
        l_op -= 1
        if l_op < 0 or l_op >= len(jsonfiles):
            raise Exception
    except:
        # os.system("clear")
        # print("\nWrong option\n")
        # input("Press enter to continue")
        return None     
    champ_f = jsonfiles[l_op][:-5].split("_")
    ch_type = champ_f[0]
    ch_name = champ_f[1]
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
    os.system("clear")
    print(my_champ)
    input("Press enter to continue")
    return my_champ

def print_fight(my_champ, enemy):
    hc = int(enemy.stats["health"] / 10) * "-"
    he = int(my_champ.stats["health"] / 10) * "-"
    print("{} {} healt: {}".format(type(enemy).__name__, enemy.name, hc))
    print()
    print("{} {} healt: {}".format(type(my_champ).__name__, my_champ.name, he))


def fight(my_champ):
    enemy = None
    e_ty = random.randint(0, 5)
    e_level = my_champ.level
    e_c_exp = random.randint(0, 5)
    e_nv_exp = 5 - e_c_exp
    e_t_exp = e_level * 5 + e_c_exp
    enemy = champ_types[e_ty]("Enemy", "Bug", "Bug", e_level, e_nv_exp, e_c_exp, e_t_exp, 0)
    os.system("clear")
    print("Your Enemy is")
    print(enemy)
    my_damage = 0
    enemy_damage = 0
    input("Press enter to continue")
    while 1:
        os.system("clear")
        # print("{} {} healt: {}".format(type(enemy).__name__,enemy.name,enemy.stats["health"]))
        # print("{} {} healt: {}".format(type(my_champ).__name__,my_champ.name,my_champ.stats["health"]))
        print_fight(my_champ, enemy)
        print("1-Attack     2-Use magic")
        try:
            f_op = int(input(">> "))
            if f_op != 1 and f_op != 2:
                raise Exception
        except:
            del enemy
            break
        if f_op == 1:
            at = my_champ.attack()
        if f_op == 2:
            at = my_champ.use_magic()
        enemy_damage = enemy.defend() - at
        # print(enemy_damage)
        if enemy_damage < 0:
            enemy.stats["health"] += enemy_damage
        
        if (enemy.stats["health"] <= 0):
            os.system("clear")
            print("\nYou win!!\n")
            my_champ.stats["health"] = 1000
            my_champ.gain_exp()
            enemy.stats["health"] = 1000
            del enemy
            input("Press enter to continue")
            break
        os.system("clear")
        print_fight(my_champ, enemy)
        time.sleep(1)
        if type(enemy) is Mage:
            at_e = enemy.use_magic()
        else:
            at_e = enemy.attack()
        my_damage = my_champ.defend() - at_e
        
        if my_damage < 0:
            my_champ.stats["health"] += my_damage
        os.system("clear")
        print_fight(my_champ, enemy)
        time.sleep(1)
        if (my_champ.stats["health"] <= 0):
            os.system("clear")
            print("\nYou loss!!\n")
            my_champ.death()
            my_champ.stats["health"] = 1000
            enemy.stats["health"] = 1000
            del enemy
            input("Press enter to continue")
            break

while 1:
    os.system("clear")
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
        os.system("clear")
        my_champ = create_champion()
        if my_champ == None:
            continue            
    if op1 == 2:
        os.system("clear")
        my_champ = load_champion()
        if my_champ == None:
            continue
    while 1:
        os.system("clear")
        print("===================================")
        print("        THE HOLBIE CHAMPION        ")
        print("===================================")
        print("1-New fight      2-Upgrade Champion")
        print("3-Save Champion  4-My Champion     ")
        print("*Any other option to go back")
        try:
            op4 =int(input(">> "))
            if not 0 < op4 < 5:
                raise Exception
        except:
            del my_champ
            break
            print()
        if op4 == 1:
            os.system("clear")
            fight(my_champ)
        if op4 == 2:
            os.system("clear")
            upgrade_champion(my_champ)

        if op4 == 3:
            os.system("clear")
            my_champ.save_character()
            print("\nChampion Saved\n")
            input("Press enter to continue")
        if op4 == 4:
            os.system("clear")
            print(my_champ)
            input("Press enter to continue")
    print()
os.system("clear")
print()


        
