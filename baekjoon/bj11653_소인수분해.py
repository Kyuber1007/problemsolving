# a = int(input())
# i = 2
# while a != 1:
#     if a % i == 0:
#         print(i)
#         a = a/i
#     else:
#         i += 1

import sys
input = int(sys.stdin.readline())
i = 2

while input > 1:
    if input % i == 0:
        print(i)
        input /= i
    else:
        i += 1