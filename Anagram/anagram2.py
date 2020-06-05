#!/usr/bin/python3
from os import path

def anagram(ana_word="holberton", n=1, ana_text="anagram.txt"):
    if type(ana_word) is not str:
        raise TypeError("word to find must be a string")
    if type(n) is not int:
        raise TypeError("path to file must be a string")
    if type(ana_word) is not str:
        raise TypeError("word to find must be a string")
    if not path.exists(ana_text):
        raise ValueError("can't find {}".format(ana_text))
    if n < 1:
        raise ValueError("number of words can't be less than 1")
    anagrams = []
    a = sorted(ana_word.lower())
    with open(ana_text) as f:
        for line in f:
            full_line = line.split()
            for i in range(0, len(full_line)):
                for j in range(1, n + 1):
                # temp = full_line[i: i + n]
                    try:
                        temp = full_line[i:i + j]
                    except:
                        continue
                    aux = a[:]
                    if j == 1:
                        string = "".join(temp)
                    else:
                        string = " ".join(temp)
                    # if len(string) != len(a) + (n - 1):
                    if len(string) != len(a) + (j - 1):
                        continue
                    for c in string:
                        if c == " ":
                            continue
                        c = c.lower()
                        if c not in aux:
                            break
                        aux.pop(aux.index(c))
                    else:
                        anagrams.append(string)
    if anagrams == []:
        print("No anagrams for '{}' in '{}'".format(ana_word, ana_text))
        return
    anagrams.sort(key = len)
    for i in anagrams:
        print(i)
    print("\n{} anagrams found\n".format(len(anagrams)))

while True:
    print("================================")
    print("Finding a Needle in the Haystack")
    print("================================")
    try:
        ana_word = input("Word to search\n>> ")
        ana_text = "anagram.txt"
        n = int(input("Maximum number of words\n>> "))
        anagram(ana_word, n, ana_text)
    except (EOFError, KeyboardInterrupt):
        break
    except Exception as e:
        print("[{}] {}". format(e.__class__.__name__, e))
print("\nBye!")
    
