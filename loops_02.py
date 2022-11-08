#!/usr/bin/python3
input_word = input("Write any word: ")
low_word = input_word.lower()
vowels = ["a", "i", "u", "e", "o", "y"]
consonents = list()
for i in low_word:
    if i not in vowels:
        consonents.append(i)


for i in range(len(consonents)):
    if i != len(consonents) - 1:
        print("{}".format(consonents[i]), end=', ')
    else:
        print("{}".format(consonents[i]))
