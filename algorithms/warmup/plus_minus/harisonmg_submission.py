#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    array_length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num == 0:
            zero += 1
        elif num < 0:
            negative += 1
        else:
            positive += 1
    print('{:.6f}'.format(positive / array_length))
    print('{:.6f}'.format(negative / array_length))
    print('{:.6f}'.format(zero / array_length))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
