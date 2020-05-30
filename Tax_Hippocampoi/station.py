Taxi = __import__('taxi').Taxi
Person = __import__('person').Person

class Station:

    def __init__(self,operator=Person("Jane Doe", "operator"), name="", ubication=""):
        self.__taxis = []
        self.__operator = operator
        self.name = name
        self.ubication = ubication

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("Please add a correct name for the station")
        self.__name = value

    @property
    def ubication(self):
        return self.__ubication

    @ubication.setter
    def ubication(self, value):
        self.__ubication = value

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        if type(value) is not Person:
            raise TypeError("Please add a correct operator")
        self.__operator = value


    def count_taxis(self):
        # print("In this station are", len(self.__taxis), "taxis")
        return len(self.__taxis)

    def add_taxi(self, taxi):
        if type(taxi) is not Taxi:
            raise TypeError("You must add only taxis to this station")
        if len(self.__taxis) < 73:
            self.__taxis.append(taxi)
        else:
            print("\u001b[31m\n --- This station is full ---\u001b[0m")

    def remove_taxi(self, client=Person("Jane Doe", "client"), trunk_size=0):
        if len(self.__taxis) == 0:
            print("0 taxis, request more")            
        if trunk_size == 0:
            print("To the client {} was asigned the Taxi:".format(client.name))
            print(self.__taxis[0])
            self.__taxis.pop(0)
            return
        for taxi in self.__taxis:
            if taxi.trunk_size >= trunk_size:
                print("To the client {} was asigned the Taxi:".format(client.name))
                print(taxi)
                self.__taxis.remove(taxi)
                return
        print("There is not a taxi with a trunk size of {}".format(trunk_size))

    def print_line(self):
        for i, taxi in enumerate(self.__taxis):
            print(i + 1,taxi)

    def __str__(self):
        string = "Station {} - Operated by {}".format(self.__name, self.__operator.name)
        h = (len(string) * "=")
        string = h + "\n" + string + "\n" + h
        return string
