import math
import sys

# reading the input
n = 0
for line in sys.stdin:
    if n == 0:
        n = int(line)
    else:
        numbers_array = [int(number) for number in line.split(' ')]

numbers_array.sort()

# calculating the mean
mean = 0
for number in numbers_array:
    mean += number
mean = mean / len(numbers_array)
print(f"{mean:.1f}")

# calculating the median
median = (numbers_array[math.ceil(n/2)-1] + numbers_array[math.ceil(n/2)])/2
print(f"{median:.1f}")

# calculating mode
prev = -1
ocurrances = 0
max_ocurrances = 0
mode = -1
for number in numbers_array:
    if prev == number:
        ocurrances += 1
        if ocurrances > max_ocurrances:
            max_ocurrances = ocurrances
            mode = number
    else:
        ocurrances = 0
    prev = number

if max_ocurrances == 0:
    mode = numbers_array[0]
print(f"{mode:.1f}")
