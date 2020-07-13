#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
from slot import Slot
from warehouse import Warehouse 
import os
import shlex


class WareHouseOP(cmd.Cmd):

    prompt = ">> "

    def __init__(self):
        super().__init__()
        self.warehouse = Warehouse()

    # def preloop(self):
    #     os.system("clear")
    # def precmd(self, line):
    #     os.system("clear")
    #     return line

    # def postcmd(self, stop, line):
    #     os.system("clear")

    def do_1(self, arg):
        """
        Show the Warehouse
        """
        self.warehouse.show(6)

    def do_cargo(self, arg):
        """
        Checks the entry cargo an evaluates if can be stored
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** mineral name missing **")
            return False
        if len(args) == 1:
            print("** mineral ammount missing **")
            return False
        mineral = args[0].lower()
        if mineral.lower() not in self.warehouse.minerals:
            print("** mineral not found **")
            return False
        try:
            ammount = eval(args[1])
            if type(ammount) is not float:
                raise Exception
        except:
            print("** ammount is not float **")
            return False
        # containers = self.warehouse.containers_ammount(mineral,ammount)
        # print(containers)
        containers = self.warehouse.allocate_cargo(mineral, ammount)
        if containers == None:
            print("There are not enough empty slots for your request")
        else:
            print("{} containers were filled with {}".format(containers, mineral))

    def do_set(self, arg):
        """
        Set a container in a slot (test only)
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** mineral name missing **")
            return False
        if len(args) == 1:
            print("** mineral ammount missing **")
            return False
        if len(args) == 2:
            print("** Slot number missing **")
            return False
        mineral = args[0].lower()
        if mineral.lower() not in self.warehouse.minerals:
            print("** mineral not found **")
            return False
        try:
            ammount = eval(args[1])
            if type(ammount) is not float:
                raise Exception
        except:
            print("** ammount is not float **")
            return False
        try:
            slot_n = eval(args[2])
            if type(slot_n) is not int:
                raise Exception
        except:
            print("** ammount is not int **")
            return False
        if self.warehouse.set_container(mineral, ammount, slot_n):
            print("1 container set with {} in the slot {}".format(mineral, slot_n))
        


    def do_EOF(self, arg):
        """
        Exit teh program
        """
        print()
        return True

if __name__ == "__main__":
    WareHouseOP().cmdloop()
