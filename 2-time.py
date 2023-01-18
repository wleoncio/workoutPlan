#!/usr/bin/python

def setWorkoutParms(superset = False):
  try:
    n_sets = int(input("Number of sets [5]: "))
  except ValueError:
    n_sets = 5
  try:
    rest_between_sets = int(input("Rest between sets [30]: "))
  except ValueError:
    rest_between_sets = 30
  if superset:
    return([n_sets, rest_between_sets])
  else:
    try:
      n_exercises = int(input("Number of exercises [6]: "))
    except ValueError:
      n_exercises= 6
    try:
      rest_between_exercises = int(input("Rest between exercises [120]: "))
    except ValueError:
      rest_between_exercises = 120
    return([n_sets, rest_between_sets, n_exercises, rest_between_exercises])

import time
import beepy
def takeBreak(t):
  while t > 0:
    print(t)
    t -= 1
    time.sleep(1)
  print(t)
  beepy.beep(sound="ping")

def runSupersetTimer(parms):
  # Defining parametes
  n_sets = parms[0]
  rest_sets = parms[1]

  # Running timer
  for s in range(n_sets - 1):
    print("Start superset number " + str(s + 1))
    input("Press enter to rest from superset number " + str(s + 1) + " of " + str(n_sets))
    takeBreak(rest_sets)
  print("Start superset number " + str(n_sets))
  print("Then your workout will be finished. Well done!")

def runRegularTimer(parms):
  # Defining parametes
  n_sets = parms[0]
  rest_sets = parms[1]
  n_exercises = parms[2]
  rest_exercises = parms[3]

  # Running timer
  for x in range(n_exercises):
    print("\nStarting exercise number " + str(x + 1) + " of " + str(n_exercises))
    for s in range(n_sets - 1):
      print("Start set number " + str(s + 1))
      input("Press enter to rest from set number " + str(s + 1) + " of " + str(n_sets))
      takeBreak(rest_sets)
    print("Start set number " + str(n_sets) + ". Last set, let's go!")
    if x < n_exercises - 1:
      input("Press enter to rest and go to the next exercise")
      takeBreak(rest_exercises)
    else:
      print("Then your workout will be finished. Well done!")

# Execution
def main():
  try:
    is_superset = bool(input("Is this workout a superset [y/N]? ") == "y")
    parms = setWorkoutParms(is_superset)
    if is_superset:
      runSupersetTimer(parms)
    else:
      runRegularTimer(parms)
  except KeyboardInterrupt:
    print("\nWorkout cancelled by user")
    exit()

main()
