import random

feet_in_miles = 5280
meters_in_kilometer = 1000


def get_file_ext(filename):
    return filename[filename.indexOf(".")+1:]


def roll_dice(num):
    return random.randint(1,num+1)