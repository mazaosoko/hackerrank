#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'gradingStudents' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        next_5 = grade // 5 * 5 + 5
        if (not grade < 38) and ((next_5 - grade) < 3):
            grade = next_5
        rounded_grades.append(grade)
    return rounded_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
