# num = input()
# i = 1
# sum = 0
# while sum < int(num):
#     sum = sum + i
#     i = i + 1
# if sum == int(num):
#     print(i - 1)
# else:
#     print(i-2)    
    
import sys
input = sys.stdin.readline

S = int(input())

N = 0
cur = 1
while S >= cur:
    S -= cur
    cur += 1
    N += 1
print(N)
