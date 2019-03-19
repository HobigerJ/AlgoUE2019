#!/bin/python3

import sys

matrix1 = []

def read_in_matrix():
    for line in sys.stdin:
        line_list = line.strip("  ").strip(" \n").split("   ")
        #print(line_list)



    return matrix1, matrix2


print(read_in_matrix())


"""
G_down: 4 5
  0.12   0.79   0.50   0.56   0.39
  0.93   0.14   0.82   0.80   0.13
  0.71   0.37   0.49   0.94   0.88
  0.59   0.52   0.40   0.87   0.16
---
G_right: 5 4
  0.43   0.21   0.55   0.61
  0.61   0.89   0.52   0.54
  0.44   0.85   0.74   0.12
  0.56   0.91   0.61   0.24
  0.56   0.42   0.27   0.49
---
"""