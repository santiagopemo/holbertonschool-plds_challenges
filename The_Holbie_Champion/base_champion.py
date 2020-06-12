#!/usr/bin/python3
import json
class BaseChampion:
    def __init__(self, name, raze, gender, level, nv_exp, current_exp, total_exp, stats, stat_points):
        self.name = name
        self.raze = raze
        self.gender = gender
        self.level = level
        self.nv_exp = nv_exp
        self.current_exp = current_exp
        self.total_exp = total_exp
        self.stats = stats
        self.stats_points = stat_points

    def level_up(self):
        if self.current_exp >= 5:
            self.total_exp += self.current_exp
            self.level += 1
            self.stats_points += 3
            self.current_exp = 0
            self.nv_exp = 5


    def gain_exp(self):
        self.current_exp += 1
        self.nv_exp -= 1
        if self.nv_exp == 0 and self.current_exp == 5:
            self.level_up()

    def death(self):
        self.current_exp /= 2

    def save_character(self):
        char_dict = {}
        char_dict["name"] = self.name
        char_dict["raze"] = self.raze
        char_dict["gender"] = self.gender
        char_dict["level"] = self.level
        char_dict["nv_exp"] = self.nv_exp
        char_dict["current_exp"] = self.current_exp
        char_dict["total_exp"] = self.total_exp
        char_dict["stats"] = self.stats
        char_dict["stat_points"] = self.stats_points
        filename = "{}_{}.json".format(type(self).__name__, self.name)
        with open(filename, mode="w") as f:
            json.dump(char_dict, f)

    @staticmethod
    def load_character(type_ch, name):
        filename = "{}_{}.json".format(type_ch, name)
        try:
            with open(filename) as f:
                return json.load(f)
        except:
            return {}

    def increase_stats(self, new_stats):
        self.stats["health"] = new_stats["health"]
        self.stats["attack"] = new_stats["attack"]
        self.stats["defense"] = new_stats["defense"]
        self.stats["magic"] = new_stats["magic"]
        self.stats["speed"] = new_stats["speed"]

    def __str__(self):
        string = ""
        string += "====================== Type =====================\n"
        string += "{} {} - {} {}\n".format(type(self).__name__, self.name, self.raze, self.gender)
        string += "=================== Experience ==================\n"
        string += "Total EXP:{} - Current EXP:{} - next level EXP:{}\n".format(self.total_exp, self.current_exp, self.nv_exp)
        string += "===================== Stats =====================\n"
        for key,value in self.stats.items():
            string +="{}: {}\n".format(key, value)
        string += "Stats points: {}\n".format(self.stats_points)
        string += "=================================================\n"
        return string