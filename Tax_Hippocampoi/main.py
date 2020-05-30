#!/usr/bin/python3
Taxi = __import__('taxi').Taxi
Station = __import__('station').Station
Person = __import__('person').Person
import random
import string

def main():
    stations = []

    stations.append(Station(Person("Santiago", "operator"), "Holberton1", "Avenida Panorama 1"))
    stations.append(Station(Person("David", "operator"), "Holberton2", "Avenida Panorama 2"))
    stations.append(Station(Person("Laura", "operator"), "Holberton3", "Avenida Panorama 3"))
    stations.append(Station(Person("Christopher", "operator"), "Holberton4", "Avenida Panorama 4"))
    app_name = "Tax Hippokampoi"
    app_header = 3 * len(app_name) * "="
    spaces = len(app_name) * " "
    hed = app_header + "\n" + spaces + app_name + spaces + "\n" + app_header
    # print(hed)
    while "pythoniscool":
        print(hed)
        print("Choose a station:")
        print_stations(stations)
        print("n--Add a new station")
        print("*type any other option to exit")
        try:
            stat_op = (input(">> "))
        except:
            break
        if stat_op == "n":
            try:
                st_name = input("Enter the name of the station\n>> ")
                st_dir = input("Enter the direction of the station\n>> ")
                st_ope = input("Enter the operators name of the station\n>> ")
                new_station = Station(Person(st_ope, "operator"), st_name, st_dir)
                stations.append(new_station)
            except:
                print("\u001b[33m\nThere was a problem adding the new station, try again\n\u001b[0m")
                continue
        else:
            try:
                stat_op = int(stat_op)
                current_st = stations[stat_op]
            except:
                break

            while "pythoniscool":                
                print(current_st)
                if current_st.count_taxis() <= 10:
                    print("\u001b[31m\nPlease request more Taxis to this location\n\u001b[0m")
                print("0-Generate new service")
                print("1-Request more taxis")
                print("2-Remaining taxis")
                print("*type any other option to go back")
                try:
                    op = int(input(">> "))
                    if op != 0 and op != 1 and op != 2:
                        raise Exception
                except:
                    print()
                    break
                if op == 0:
                    if current_st.count_taxis() == 0:
                        print("\u001b[31m\n0 taxis remaining, request for more\n\u001b[0m")
                        continue
                    try:
                        client = input("Enter clients name\n>> ")
                        trunk = int(input("Enter the lugage size\n>> "))
                    except:
                        print("\u001b[33m\nThere was a problem generating the new service try again\n\u001b[0m")
                        continue
                    print()
                    current_st.remove_taxi(Person(client, "client"), trunk)
                    print()
                    
                if op == 1:
                    generate_taxis(current_st)
                if op == 2:
                    current_st.print_line()
                    print("\u001b[33m\nIn this station are", current_st.count_taxis(), "taxis\n\u001b[0m")
    
        
        

def print_stations(stations=[]):
    for i in stations:
        print("{}--{}".format(stations.index(i), i.name))

def generate_taxis(station):
    if station.count_taxis() >= 72:
        n_taxis = 1
    else:
        n_taxis = random.randrange(73 - station.count_taxis())
    for i in range(n_taxis):
        N = 5
        plates = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        driver_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(9))
        trunk_size = random.randrange(0, 100, 20)
        cilinder = random.randrange(1000, 3000, 200)
        station.add_taxi(Taxi(plates, trunk_size, Person(driver_name, "driver"), cilinder))
    if station.count_taxis() == 73:
        n_taxis = 0
    print("\n{} taxis has arrived, for a total of {} taxis\n".format(n_taxis, station.count_taxis()))

main()
