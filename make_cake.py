#!/usr/bin/python3

def isTooSweet(i):
    if i >= 5:
        return True
    return False

def make_cake(n):
    if isTooSweet(n):
        while (isTooSweet(n) == True):
            n -= 1
        n += 1
    print("number of teespoons {}".format(n))

def make_cake_binary(n):
    low = 0
    high = n
    spoons = 0
    while (1):
        mid = int(low + (high - low) / 2)
        if isTooSweet(mid):
            if isTooSweet(mid - 1) == False:
               spoons = mid
               break
            high = mid - 1            
        if isTooSweet(mid) == False:
            if isTooSweet(mid + 1):
               spoons = mid + 1
               break
            low = mid + 1 
    print("number of teespoons {}".format(spoons))

def make_cake_binary2(n):
    low = 0
    high = n
    spoons = 0
    while (1):
        if low == high:
            spoons = mid
            break
        mid = int(low + (high - low) / 2)
        if isTooSweet(mid):
            high = mid - 1            
        if isTooSweet(mid) == False:
            low = mid + 1 
    print("number of teespoons {}".format(spoons))


def main():
    make_cake_binary(6)
    make_cake_binary2(6)

main()

