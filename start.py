#!/usr/bin/python3
import os
from os.path import exists, expanduser
import sys

def get_log_path ():
  try:
    home_folder = expanduser("~")
    config_location = home_folder + "/.config/workoutPlan.conf"
    stream = open(config_location, "r")
    if exists(config_location):
      log_path = home_folder +"/"+ stream.readline().strip("LOGPATH=~")
      log_path = log_path.strip()
      return log_path
  except FileNotFoundError as e:
    sys.exit("No config file found to determine LOGPATH")


def select_option ():
  prompt = "1.Choose\n2.Time\n3.Log\n4.History\n5.Catalog\n6.Quit\nSelect step: "
  option = str(input(prompt))
  log_path = (get_log_path())
  script_dict = {"1":"1-choose.py","2":"2-time.py","3":"3-log.py","4":"history.py","5":"history.py abc"}
  if option in script_dict:
    invoke_script = (log_path + "/" + script_dict[option])
    os.system('python3 ' + invoke_script)
    return "Y"
  elif option == "6":
    return "N"
  else:
    print("Invalid Option\n")
    return "Y"




#Invoke function
ask_again = (select_option())

#Ask user to provide input again,  if input is not proper
while ask_again != "N":
  ask_again = (select_option())
