# Suppose that you were painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, write a python code to calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.

import math
def paint_calc(height, width, cover):
  number_of_cans = (height*width)/cover
  print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

test_h = int(input("What is the height(m) of the wall?\n")) # Height of wall (m)
test_w = int(input("What is the width(m) of the wall?\n")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
