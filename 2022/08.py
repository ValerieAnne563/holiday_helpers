"""
https://adventofcode.com/2022/day/8#part2
"""

import numpy as np
import logging

test_input = [
   "30373",
   "25512",
   "65332",
   "33549",
   "35390"
   ]


# forest = np.array([[int(x) for x in row] for row in test_input])

with open("input_08.txt") as f:
   forest = np.array([[int(x) for x in row.strip()] for row in f.readlines()])

print(forest)

visible = np.zeros(shape=forest.shape)
numrows, rowlen = forest.shape

# Search horizontally, include all edge trees
for r in range(0, numrows):
   row = forest[r]
   left_max = -1
   right_max = -1

   left_max = row[0]
   right_max = row[rowlen-1]
   for c in range(0, rowlen):

      # Edges are always visible
      if r == 0 or c == 0:
         visible[r][c] = True
         continue
      elif r == numrows - 1 or c == rowlen - 1:
         visible[r][c] = True
         continue

      # Check left to right visibility
      ltr_height = row[c]
      if ltr_height > left_max:
         visible[r][c] = 1
         logging.info("(%d,%d) is visible from the left: %d <= %d", r, c, ltr_height, left_max)
         left_max = ltr_height

      # Check right to left visibility
      _c = rowlen - c - 1
      rtl_height = row[_c]

      if rtl_height > right_max:
         visible[r][_c] = 1
         logging.info("(%d,%d) is visible from the right: %d <= %d", r, _c, rtl_height, right_max)
         right_max = rtl_height


# Search vertically
for c in range(0, rowlen):
   top_max = -1
   bottom_max = -1

   top_max = forest[0][c]
   bottom_max = forest[numrows-1][c]
   for r in range(0, numrows):

      # Check top to bottom  visibility
      ttb_height = forest[r][c]
      if ttb_height > top_max:
         visible[r][c] = 1
         logging.info("(%d,%d) is visible from the top: %d <= %d" , _r, c, ttb_height, top_max)
         top_max = ttb_height

      # Check right to left visibility
      _r = numrows - r - 1
      btt_height = forest[_r][c]

      if btt_height > bottom_max:
         visible[_r][c] = 1
         logging.info("(%d,%d) is visible from below: %d <= %d" ,_r, c, btt_height, bottom_max)
         bottom_max = btt_height


# for row in visible:
#    print(row)

print("Number of visible trees: %d" % np.sum(visible))
