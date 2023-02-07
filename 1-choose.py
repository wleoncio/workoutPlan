#!/usr/bin/python3
url = "https://www.darebee.com/filter#sort=position&sortdir=desc&page=1"

print("# Filtering\n")
# Processing name
name = input("Exercise name: ")
if name != "":
  url+= "&name=" + name
else:
  # Processing focus
  focus_num = input("Choose focus ([u]pper, [a]bs, [l]ower, [f]ull): ")
  focus_dic = {"f": "full-body", "u": "upper-body", "l": "lower-body", "a": "abs"}
  if focus_num != "":
    focus_url = "&attr.ct10.value=" + focus_dic[focus_num]
    url += focus_url

  # Processing type
  type_url = "&attr.ct16.value=strength"
  url += type_url

  # Processing difficulty
  difficulty_num = input("Choose difficulty (1-5): ")
  difficulty_dic = {1: "light", 2: "easy", 3: "normal", 4: "hard", 5: "advanced"}
  if difficulty_num != "":
    difficulty_num = int(difficulty_num)
    difficulty_url = "&attr.ct14.value=" + difficulty_dic[difficulty_num]
    url += difficulty_url

  # Processing equipment
  equipment_num = input("Choose equipment (1 none, 2 dumbbells, 3 pull-up bar): ")
  equipment_dic = {1: "none", 2: "dumbbells", 3: "bar"}
  if equipment_num != "":
    equipment_num = int(equipment_num)
    equipment_url = "&attr.ct19.value=" + equipment_dic[equipment_num]
    url += equipment_url

  # Output
  print("\n# Suggesting exercises\n")
  print("Focus:      " + (focus_dic[focus_num] if focus_num != "" else "all"))
  print("Type:       strength")
  print("Difficulty: " + (difficulty_dic[difficulty_num] if difficulty_num != "" else "all"))
  print("Equipment:  " + (equipment_dic[equipment_num] if equipment_num != "" else "all"))
  print()

import os
os.system("firefox \"" + url + "\" &\n")
