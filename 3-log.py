#!/usr/bin/python
from os.path import exists

class Exercise:
  def __init__(self, url, folder="log"):
    base_url = "https://www.darebee.com/workouts/"
    suffix = "-workout.html"
    self.__file_html_name = url.replace(base_url, "")
    self.exercise_name = self.__file_html_name.replace(suffix, "")
    self.file_name = folder + "/" + self.exercise_name + ".csv"
    if exists(self.file_name):
      self.read()
    to_save = input("Save new workout [y/N]?: ")
    if to_save == "y":
      self.save()

  def __str__(self):
    print(self.exercise_name)

  def save(self):
    # Gathering data
    self.date = input("Enter date: ")
    self.level = input("Enter level: ")
    self.pause = input("Enter pause: ")
    self.weight = input("Enter weight: ")
    self.difficulty = int(input("Enter difficulty (1 too easy, 2 ok, 3 too hard): "))
    difficulty_dic = {1 : "Too easy", 2 : "OK", 3 : "Too hard"}
    self.difficulty = difficulty_dic[self.difficulty]
    
    # Saving data
    stream = open(self.file_name, "at")
    line = self.date + "," + self.level + "," + self.pause + "," + self.weight + "," + self.difficulty + "\n" 
    stream.write(line)
    stream.close()

  def read(self):
    stream = open(self.file_name, "rt")
    print("Date\t\tLevel\tPause\tWeights")
    for line in stream:
      line_split = line.split(",")
      line_string = '\t'.join(line_split).replace("\n","")
      print(line_string)
    stream.close()

# Executing
this_url = input("Enter exercise URL: ")
Exercise(this_url)
