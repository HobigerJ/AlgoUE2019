#!/bin/python3

import sys

matrix1 = []

def read_in_matrix():
    for line in sys.stdin:
        if line.startswith("G"):
            continue

        if line.startswith("---"):
            break
        print(line)
        


print(read_in_matrix())


uebungs_matrix = [[1,2,3], 
                  [4,5,6], 
                  [7,8,9]]