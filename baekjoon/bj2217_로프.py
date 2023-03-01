import sys

input = sys.stdin.readline
N = int(input())

ropes = []

weight_sum = 0

for i in range(N):
    weight = int(input())
    ropes.append(weight)

ropes.sort(reverse=True)

# 순서대로 돌아가면서 현재 값과 갯수를 곱해서 최대 들 수 있는 무게를 계산함.
max = ropes[0]
for i in range(1, N):
    cur_possible = ropes[i] * (i + 1)
    if cur_possible > max:
        max = cur_possible

print(max)
