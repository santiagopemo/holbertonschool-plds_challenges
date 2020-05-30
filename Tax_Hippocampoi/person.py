#!/usr/bin/python3
class Person:

    def __init__(self, name="Jon Doe", rol="client"):
        self.name = name
        self.rol = rol

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is str:
            self.__name = value
        else:
            raise TypeError("Name must be a string")

    @property
    def rol(self):
        return self.__value

    @rol.setter
    def rol(self, value):
        """ 
            Rols:
            operator
            client 
            driver
        """
        if type(value) is str:
            self.__rol = value
        else:
            raise TypeError("rol must by a string")

    def __str__(self):
        return "I am {} a {}".format(self.__name, self.__rol)
