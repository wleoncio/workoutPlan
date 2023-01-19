#!/usr/bin/python
from os.path import exists
import datetime

path="log/"
file="day.csv"

# Create file, if necessary
if not exists(path + file):
    print("Daily log not found. Creating...")
    stream = open(path + file, "xt")

# Reading content
stream = open(path + file, "rt")
print("Date\t\tUpper\tAbs\tLower\tCardio")
for line in stream: # TODO: DRY (same code in Exercise class)
    line_split = line.split(",")
    line_string = '\t'.join(line_split).replace("\n","")
    print(line_string)
stream.close()

# Reading new content
today = datetime.datetime.now().strftime("%Y-%m-%d")
date = input("Enter date (if different from " + today +"): ") # TODO: DRY (same code in Exercise class)
if date == "":
 date = today
did_upper = input("Worked upper body [y/N]? ") != "n"
did_abs = input("Worked abs [y/N]? ") != "n"
did_lower = input("Worked lower body [y/N]? ") != "n"
did_cardio = input("Did cardio [y/N]? ") != "n"

# Saving data
stream = open(path + file, "at")
new_line = ','.join([str(date), str(did_upper), str(did_abs), str(did_lower), str(did_cardio)]) + "\n"
stream.write(new_line)
stream.close()
