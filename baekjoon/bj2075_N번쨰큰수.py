import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

n = int(input())
num_list = []

for i in range(n):
    new_int = map(int, input().split())
    for number in new_int:
        if len(num_list) >= n:
            if num_list[0] < number:
                heappop(num_list)
                heappush(num_list, number)
        else:
            heappush(num_list, number)
      
print(num_list[0])