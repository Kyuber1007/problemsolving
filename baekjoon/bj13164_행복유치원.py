import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

members = list(map(int, input().split()))

diffs = []
for i in range(1, N):
    heapq.heappush(diffs, members[i] - members[i - 1])

count = 0

# 골라야 하는 차이의 갯수를 생각하자!
for i in range(N - K):
    count += heapq.heappop(diffs)
print(count)
