import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip_cost = tip_percent * 0.01 * meal_cost
    tax_cost = tax_percent * 0.01 * meal_cost
    total_cost = meal_cost + tip_cost + tax_cost
    return round(total_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    total_cost = solve(meal_cost, tip_percent, tax_percent)
    print(total_cost)
