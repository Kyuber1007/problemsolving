import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())

card_dummies = []
for i in range(N):
    heappush(card_dummies, int(input()))

result = 0

while len(card_dummies) > 1:
    x1 = heappop(card_dummies)
    x2 = heappop(card_dummies)
    result += x1 + x2
    heappush(card_dummies, x1+x2)

print(result)
