#!/usr/bin/python3
"""Warehouse Module"""
from slot import Slot
from container import Container
import math
import uuid


class Warehouse:
    """Warehouse Class"""

    minerals = {
        'copper': 2,
        'feldspar': 1,
        'lithium': 0.75,
        'silver': 2,
        'gold': 0.75,
        'iron ore': 1.5,
        'lead': 1,
        'nickel': 2,
        'beryllium': 0.5,
        'molybdenum': 1,
    }

    def __init__(self, size=30):
        self.size = size
        self.slots = []
        for i in range(self.size):
            self.slots.append(Slot())
        # u_id = str(uuid.uuid4())
        # self.slots[5].container = Container(u_id, 5, 'lead', 1.0, "santiago123")    

    def show(self, l):
        c = 0
        for i in range(0, self.size, l):
                      
            for j in range(l):
                try: 
                    h = "+-" + len(self.slots[i + j].__str__()) * "-" + "-+"
                    print(h + " ", end="")            
                except IndexError:
                    break
            print()
            for j in range(l):
                try:
                    print("| {} | ".format(self.slots[i + j]), end="")
                except IndexError:
                    break
            print()
            for j in range(l):
                try:
                    h = "+-" + len(self.slots[i + j].__str__()) * "-" + "-+"
                    print(h + " ", end="")
                except IndexError:
                    break
            print()

    def containers_ammount(self, mineral, cargo):
        return math.ceil(cargo / Warehouse.minerals[mineral])

    def allocate_cargo(self, mineral, cargo):
        containers = math.ceil(cargo / Warehouse.minerals[mineral])
        for i in range(len(self.slots)):
            for j in range(containers):
                try:
                    if self.slots[i + j].container != None:
                        break
                except IndexError:
                    break
            else:
                u_id = str(uuid.uuid4())
                for k in range(containers):
                    c_id = "{}_{}".format(u_id, k)
                    c_weight = cargo / containers
                    self.slots[i + k].container = Container(c_id, self.slots[i + k].id, mineral, c_weight, "santiago123")
                return containers
        else:
            return None

    def set_container(self, mineral, ammount, slot):
        if slot < len(self.slots):
            c_id = str(uuid.uuid4())
            self.slots[slot].container = Container(c_id, self.slots[slot].id, mineral, ammount, "santiago123")
            return True
        return False
