#!/usr/bin/python3
Person = __import__('person').Person
class Taxi:
    def __init__(self, plates="", trunk_size=0, driver=Person("Jhon Doe", "driver"), cilindre_c=0):
        self.plates = plates
        self.trunk_size = trunk_size
        self.driver = driver
        self.cilindre_c = cilindre_c

        @property
        def plates(self):
            return self.__plates

        @plates.setter
        def plates(self, value):
            if type(value) is not str:
                raise TypeError("Plate Taxi must be a string")
            self.__plates = value

        @property
        def trunk_size(self):
            return self.__trunk_size

        @trunk_size.setter
        def trunk_size(self, value):
            if type(value) is not int:
                raise TypeError("Trunk Size Taxi will be a integer")
            self.__trunk_size = value

        @property
        def driver(self):
            return self.__driver

        @driver.setter
        def driver(self, value):
            """ setter driver """
            if type(value) is not Person:
                raise TypeError("Taxi Driver must be a string")
            self.__driver = value

        @property
        def cilindre_c(self):
            return self.__cilindre_c

        @cilindre_c.setter
        def cilindre_c(self, value):
            """ setter cilindre_c """
            if type(value) is not int:
                raise TypeError("Cilindre Taxi must be a integer")
            self.__cilindre_c = value

    def __eq__(self, other):
        return self.plates == other.plates

    def __str__(self):
        return "Plates: {} - Driver: {} - Trunk: {} - Cilinder: {}".format(self.plates, self.driver.name, self.trunk_size, self.cilindre_c)
