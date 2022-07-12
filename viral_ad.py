#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    if n >= 1 and n <= 50:
        i = 1
        shared = 5
        liked = 2
        cml = 2
    
        while i < n:
            shared = liked * 3
            liked = int(shared / 2)
            cml = cml + liked
            i = i + 1
        
        return cml
    
    else:
        return "Please enter a value within 1 and 50"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
