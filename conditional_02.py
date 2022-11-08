#!/usr/bin/python3
m = input("Name any month: ")
months_with_31days = ["January", "March", "May", "July", "August", "October", "December"]
months_with_30days = ["April", "June", "September", "November"]
if m in months_with_31days:
    print("The month of {} has 31 days.".format(m))
elif m == "February":
    print("The month of {} has 28 or 29 days.".format(m))
elif m in months_with_30days:
    print("The month of {} has 30 days.".format(m))
