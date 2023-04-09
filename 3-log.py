#!/usr/bin/python3
from os.path import exists, expanduser
import datetime

class Exercise:
  def __init__(self, url, folder="log"):
    base_urls = ["https://www.darebee.com/workouts/", "https://darebee.com/workouts/"]
    suffix = "-workout.html"
    self.__file_html_name = url.replace(base_urls[0], "").replace(base_urls[1], "")
    self.exercise_name = self.__file_html_name.replace(suffix, "")
    self.file_name = folder + "/" + self.exercise_name + ".csv"
    if exists(self.file_name):
      self.read()
    to_save = input("Save new workout [y/N]?: ")
    if to_save == "y":
      self.save()
      print("\nUpdated log")
      self.read()

  def __str__(self):
    print(self.exercise_name)

  def save(self):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # Gathering data
    self.date = input("Enter date (if different from " + today +"): ")
    if self.date == "":
        self.date = today
    self.level = input("Enter level: ")
    self.pause = input("Enter pause: ")
    self.weight = input("Enter weight: ")
    self.difficulty = input("Enter comment (shortcuts: 1 too easy, 2 ok, 3 too hard): ")
    if self.difficulty in ["1", "2", "3"]:
      difficulty_dic = {1 : "Too easy", 2 : "OK", 3 : "Too hard"}
      self.difficulty = difficulty_dic[int(self.difficulty)]


    # Saving data
    stream = open(self.file_name, "at")
    line = self.date + "," + self.level + "," + self.pause + "," + self.weight + "," + self.difficulty + "\n"
    stream.write(line)
    stream.close()

  def read(self):
    stream = open(self.file_name, "rt")
    print("Date\t\tLevel\tPause\tWeights\tPerformance")
    for line in stream:
      line_split = line.split(",")
      line_string = '\t'.join(line_split).replace("\n","")
      print(line_string)
    stream.close()

def addURL(name):
    return("https://darebee.com/workouts/" + name + "-workout.html")

def expandFolder(letter):
    match letter:
        case "u":
            return "upper"
        case "l":
            return "lower"
        case "a":
            return "abs"
        case "f":
            return "full"

# Parsing exercise name and location

this_subfolder = expandFolder(input("Enter focus [f/u/a/l]: "))
this_url = input("Enter exercise URL/CSV name: ")

# Checking for location of log folder in config file
home_folder = expanduser("~")
config_location = home_folder + "/.config/workoutPlan.conf"
if exists(config_location):
    stream = open(config_location)
    log_path = home_folder + stream.readline().strip("LOGPATH=~")
    stream.close()
    log_path = log_path.strip("\n")
    this_subfolder = log_path + "/log/" + this_subfolder
    print(this_subfolder)

# Parsing non-URLs
if this_url[0:4] != "http":
    this_url = addURL(this_url)

Exercise(this_url, this_subfolder)
