# import sys

# A, B, C, M = map(int, sys.stdin.readline().split())
# hours = 0
# tiredity = 0
# work = 0

# while hours < 24:
#     if tiredity + A <= M:
#         work += B
#         tiredity += A
#     else:
#         tiredity -= C
#     if tiredity < 0:
#         tiredity = 0
#     hours += 1

# print(work)

import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

works = 0
tiredity = 0

for i in range(24):
    if tiredity + A > M:
        tiredity -= C
        if tiredity < 0:
            tiredity = 0
    else:
        works += B
        tiredity += A
print(works)
