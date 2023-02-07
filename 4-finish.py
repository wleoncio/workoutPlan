#!/usr/bin/python3
from os.path import exists
import datetime
import termcolor

path="log/"
file="day.csv"

# Create file, if necessary
if not exists(path + file):
    print("Daily log not found. Creating...")
    stream = open(path + file, "xt")

# Reading content
stream = open(path + file, "rt")
print("Date\t\tUpper\tAbs\tLower\tCardio")
streak_upper = []
streak_abs = []
streak_lower = []
streak_cardio = []
for line in stream: # TODO: DRY (same code in Exercise class)
    line_split = line.split(",")
    streak_upper.append(line_split[1] == 'True')
    streak_abs.append(line_split[2] == 'True')
    streak_lower.append(line_split[3] == 'True')
    streak_cardio.append(line_split[4] == 'True\n')

    # Runtime coloring of True and False
    for l in range(len(line_split)):
        if line_split[l] in ["True", "True\n"]:
            line_split[l] = termcolor.colored("True", "green")
        elif line_split[l] in ["False", "False\n"]:
            line_split[l] = termcolor.colored("False", "red")

    line_string = '\t'.join(line_split).replace("\n","")
    print(line_string)
stream.close()

def calcStreak(x):
    x.reverse()
    done_streak = 0
    for element in x:
        if element:
            done_streak += 1
        if not element:
            break
    rest_streak = 0
    for element in x:
        if not element:
            rest_streak +=1
        else:
            break
    return([done_streak, rest_streak])

print('Upper streak  [done, rest]: ' + str(calcStreak(streak_upper)))
print('Abs streak    [done, rest]: ' + str(calcStreak(streak_abs)))
print('Lower streak  [done, rest]: ' + str(calcStreak(streak_lower)))
print('Cardio streak [done, rest]: ' + str(calcStreak(streak_cardio)))

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
