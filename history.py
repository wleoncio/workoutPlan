#!/usr/bin/python3
from os.path import exists, expanduser
import sys
import subprocess

#Fetch LOGPATH into variable "log_path"
def get_log_path():
  try:
    home_folder = expanduser("~")
    config_location = home_folder + "/.config/workoutPlan.conf"
    stream = open(config_location, "r")
    if exists(config_location):
      log_path = home_folder + stream.readline().strip("LOGPATH=~")
      log_path = log_path.strip()
      return log_path
  except FileNotFoundError as e:
    sys.exit("No config file found to determine LOGPATH")

def  display_files(arg1):
  log_path = get_log_path()
  if arg1 == "abc":
    print("Sorting alfabetically")
    command = ["-i", "--dirsfirst", "-C"]
  else:
    print("Sorting by time")
    command = ["-t", "--timefmt", "%a %d-%b", "--noreport", "-C"]
  subprocess.run(["tree", log_path] + command)

if len(sys.argv) == 2:
  display_files(sys.argv[1])
else:
  display_files("Time")
