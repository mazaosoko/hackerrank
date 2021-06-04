#!/bin/python3

import os
import sys


# Complete the timeConversion function below.
def timeConversion(s):
    hh, mm, ss_am_pm = s.split(':')
    hh = int(hh)
    ss = ss_am_pm[:2]
    am_pm = ss_am_pm[2:]
    if (am_pm == 'PM') and (hh != 12):
        hh += 12
    elif (am_pm == 'AM') and (hh == 12):
        hh -= 12
    return '{:02d}:{}:{}'.format(hh, mm, ss)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
