import sys

input = sys.stdin.readline

N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

result = 0

for i, value in enumerate(nums):
    if value - i < 0:
        break
    result += value - i
print(result)
