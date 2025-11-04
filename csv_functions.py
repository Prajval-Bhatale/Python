#csv functions

import pandas as pd

info = pd.read_csv("student.csv")

print(info.head(3))                         #print starting 3 data
print("\n---------------------------\n")

print(info.tail(3))                         #print last 3 data
print("\n---------------------------\n")

print(info.describe())                       #print min max per
print("\n---------------------------\n")

print(info.columns)                             #display columns names in list form
print("\n---------------------------\n")

print(info['Roll No'])                                #print specific information in[]




