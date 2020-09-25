#!/usr/bin/python3
"""
Define lf the list of fields and lt the list of towers
Create a list called res of n times 10^9 (n = number of fields)
Create 2 pointers for each list: i for the list of fields / j for the list of towers and set them to 0
Loop while i < size of lf and j < size of lt
    If lf[i] <= lt[j]
        res[i] = lt[j] - lf[i] and i ++
    Else
        j ++
Reuse i and j:
i = size of lf - 1
j = size of lt - 1
Loop while i >= 0 and j >= 0
    If lf[i] >= lt[j]
        res[i] = lf[i] - lt[j] if this new value is under the one presents in res[i]
        i --
    Else
        j --
Return the max value of res
"""

def closest_water_tower(lf, lt):
    i = 0
    j = 0
    res = [ 10 ** 9 ] * len(lf) 
    while (i < len(lf) and j < len(lt)):
        if lf[i] <= lt[j]:
            res[i] = lt[j] - lf[i] 
            i += 1
        else:
            j += 1
    i = len(lf) - 1
    j = len(lt) - 1
    while (i >= 0 and j >= 0):
        if lf[i] >= lt[j]:
            if lt[j] < res[i]:
                res[i] = lf[i] - lt[j]
            i -= 1
        else:
            j -= 1
    print(res)
    return max(res)

def main():
    Fields = [1, 2, 3]
    Towers = [2]
    print(closest_water_tower(Fields, Towers))
    Fields = [1, 2, 3, 4]
    Towers = [1, 4] 
    print(closest_water_tower(Fields, Towers))
    Fields = [1, 5]
    Towers = [10]
    print(closest_water_tower(Fields, Towers))
    Fields = [1, 2, 3, 4, 5]
    Towers = [4]
    print(closest_water_tower(Fields, Towers))

main()
