import sys
input = sys.stdin.readline

n = int(input())

from heapq import heappop, heappush

neg_heap = []
posi_heap = []

for i in range(n):
    new_int = int(input())
    if new_int == 0:
        # pop 최소 숫자
        if len(posi_heap) == 0 and len(neg_heap) == 0:
            print(0)
        elif len(posi_heap) == 0:
            print(heappop(neg_heap) * -1)
        elif len(neg_heap) == 0:
            print(heappop(posi_heap))
        elif posi_heap[0] < neg_heap[0]:
            print(heappop(posi_heap))
        else:
            print(heappop(neg_heap) * -1)
    elif new_int > 0:
        heappush(posi_heap, new_int)  
    else:
        heappush(neg_heap, new_int * -1) 
