#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    aux = 0
    for i in range(n-1):
        if ar[i]==0:
            continue
        for x in range(i+1,n):
            if ar[x]==ar[i]:
                aux = aux + 1
                ar[x] = 0
                ar[i] = 0
                break
    return aux

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
