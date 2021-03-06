#!/usr/bin/python3
import random
from base_champion import BaseChampion

class Rogue(BaseChampion):
    attack_weapon = {"name": "daggers", "value": 40}
    def_equ = {"name": "None", "value": 0}
    armor = ["Chest armor"]
    init_stats = {"health": 1000, "attack": 15, "defense": 15, "magic": 5, "speed": 25}

    def __init__(self, name, race, gender, level, nv_exp, current_exp, total_exp, stat_points):
        
        super().__init__(name, race, gender, level, nv_exp, current_exp, total_exp, type(self).init_stats.copy(), stat_points)

    def attack(self):
        atack_speed = 1 + self.stats["speed"] / (len(type(self).armor) * 2 + 1)
        totalAtack = self.stats["attack"] * atack_speed + type(self).attack_weapon["value"]
        return totalAtack * (random.random() + .5)


    def defend(self):
        totalDef = self.stats["defense"] + (1 + (len(type(self).armor) * 20)) + type(self).def_equ["value"]
        return totalDef * (random.random() + .5)

    def use_magic(self):
        return self.stats["magic"] * (random.random() + .5)
