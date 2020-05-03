#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    stack = ['h','a','c','k','e','r','r','a','n','k']
    index = 0
    for i in s:
        if index == 9:
            return ('YES')
            break
        if i == stack[index]:
            index += 1
    return ('NO')

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
