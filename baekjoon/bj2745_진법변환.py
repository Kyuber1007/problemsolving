import sys

input = sys.stdin.readline().split()
number = 0
old_arithmetic = int(input[1])
i = len(input[0]) - 1

for value in input[0]:
    if value.isalpha():
        cur = ord(value) - 55
    else:
        cur = int(value)
    number += cur * (old_arithmetic ** i)
    i -= 1
    
print(number)