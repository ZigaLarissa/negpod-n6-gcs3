#!/usr/bin/python3
num = int(input("Write any integer: "))
numbers = list()
for i in range(num + 1):
    if i % 2 != 0:
        numbers.append(i)


for i in numbers:
    if i != numbers[-1]:
        print("{}".format(i), end=', ')
    else:
        print("{}".format(i))
