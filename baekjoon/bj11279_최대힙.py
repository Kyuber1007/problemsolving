import sys
input = sys.stdin.readline

n = int(input())

from heapq import heappop, heappush

heap = []
for i in range(n): 
    new_int = int(input())
    if new_int == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    heappush(heap, (-new_int, new_int))
 