import sys
strings = sys.stdin.readline().strip().split('-')
result = 0
for i, string in enumerate(strings):
    numbers = list(map(int, string.split('+')))
    tem = 0
    for j in numbers:
        tem += j
    if i == 0:
        result += tem
    else:
        result -= tem
print(result)
