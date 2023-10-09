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
 option=str(input("1.Choose\n2.Time\n3.Log\n4.History\n5.Catalog\nSelect step: "))
 log_path=(get_log_path())
 script_dict={"1":"1-choose.py","2":"2-time.py","3":"3-log.py","4":"history.py","5":"history.py abc"}
 cnt=0
 for key  in script_dict: 
  cnt+=1  
  if key == option: 
   invoke_script=(log_path +"/"+ script_dict[key]) 
   os.system('python3 '+ invoke_script)
   cnt=0

 if cnt == len(script_dict):
  print("Invalid Option")
  return "Y"
 else:
  return "N"
 
 

#Invoke function
ask_again=(select_option())

#Ask user to provide input again,  if input is not proper
while ask_again != "N":
 ask_again=(select_option())


