# module is a python file that we can use inside another python file

from useful_tool import *  #import all the things from the user_tool python file

import useful_tool
print(useful_tool.feet_in_miles)
print(useful_tool.roll_dice(10))

# pip is a program to install python modules
# it is like package manager
