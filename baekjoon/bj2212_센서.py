import heapq
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

places = list(map(int, input().split()))

places.sort()

diffs = []
for i in range(1, N):
    heapq.heappush(diffs, places[i] - places[i - 1])

result = 0
for i in range(N - K):
    result += heapq.heappop(diffs)
print(result)
