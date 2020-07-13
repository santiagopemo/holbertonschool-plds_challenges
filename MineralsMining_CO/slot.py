#!/usr/bin/env python3
"""
Slot Module
"""
from container import Container


class Slot:
    """Container Class"""
    __id = 0
    def __init__(self, container=None):
        self.id = Slot.__id
        Slot.__id += 1
        self.container = container

    def __str__(self):
        if self.container:
            return "{:^10}".format(self.container.mineral_type.upper())
        else:
            return "Slot {:>5}".format(self.id)

    def remove_container(self):
        del self.container
        self.container = None

# s1 = Slot()
# s2 = Slot()
# print(s1.id)
# print(s2.id)
# print(s1.id)
# print(Slot._Slot__id)
