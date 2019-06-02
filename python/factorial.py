# Task 
# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

# Input Format
# A single integer, N (the argument to pass to factorial).

# Constraints
# 2 <= N <= 12
# Your submission must contain a recursive function named factorial.

# Output Format
# Print a single integer denoting N!.

# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):

    f =1
    num = n

    if num == 1:
        return f

    while num >0:
        f = f * num
        num = num -1

    return f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
