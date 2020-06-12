#!/usr/bin/python3
import random
from base_champion import BaseChampion

class Fighter(BaseChampion):
    attack_weapon = {"name": "sword", "value": 50}
    def_equ = {"name": "shield", "value": 50}
    armor = ["Helmet", "Gauntlets", "Chest armor", "Leg armor"]
    init_stats = {"health": 100, "attack": 100, "defense": 100, "magic": 100, "speed": 100}

    def __init__(self, name, raze, gender, level, nv_exp, current_exp, total_exp, stat_points):
        
        super().__init__(name, raze, gender, level, nv_exp, current_exp, total_exp, type(self).init_stats, stat_points)

    def attack(self):
        atack_speed = 1 + self.stats["speed"] / (len(type(self).armor) * 10 + 1)
        totalAtack = self.stats["attack"] * atack_speed + type(self).attack_weapon["value"]
        return totalAtack * (random.random() + .5)


    def defend(self):
        totalDef = self.stats["defense"] + (1 + (len(type(self).armor) * 20)) + type(self).def_equ["value"]
        return totalDef * (random.random() + .5)

    def use_magic(self):
        return self.stats["magic"] * (random.random() + .5)

class Solar(Fighter):

    champ_type = "solar"
    stats = {"power": "fire ball", "afinity": "fire"}

    def __init__(self, name, race, gender, level, nv_exp, current_exp, total_exp, stat_points):
        super().__init__(name, race, gender, level, nv_exp, current_exp, total_exp, stat_points)
        self.stats["power"] = type(self).stats["power"]
        self.stats["afinity"] = type(self).stats["afinity"]
    
    def skill(self, enemy):
        if type(self) is Solar and type(enemy) is Solar:
            return super().attack * 1
        if type(self) is Solar and type(enemy) is Arc:
            return super().attack * 1.25
        if type(self) is Solar and type(enemy) is Void:
            return super().attack * 0.75
        if type(self) is Arc and type(enemy) is Arc:
            return super().attack * 1
        if type(self) is Arc and type(enemy) is Solar:
            return super().attack * 0.75
        if type(self) is Arc and type(enemy) is Void:
            return super().attack * 1.25
        if type(self) is Void and type(enemy) is Void:
            return super().attack * 1
        if type(self) is Void and type(enemy) is Solar:
            return super().attack * 1.25
        if type(self) is Void and type(enemy) is Arc:
            return super().attack * 0.75
