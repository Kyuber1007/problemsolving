import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
num_heap = []

for i in range(n):
    new_number_list = map(int, input().split())
    for number in new_number_list:
        if len(num_heap) < n:
            heappush(num_heap, number)
        else:
            if num_heap[0] < number:
                heappop(num_heap)
                heappush(num_heap, number)
print(num_heap[0])