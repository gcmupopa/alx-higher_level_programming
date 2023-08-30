#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
split_str = str.split(", ")
print(split_str[2].split(" that ")[0], str.split()[12], str.split()[0])
