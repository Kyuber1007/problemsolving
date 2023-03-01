import sys
from heapq import heappush

input = sys.stdin.readline

n, k = map(int, input().split())

erased_list = []
count = 0

for i in range(2, n + 1):
    j = 1
    num = i * j
    while count < k and num <= n:
        if num not in erased_list:
            erased_list.append(num)
            count += 1
        j += 1
        num = i * j
    if count == k:
        break
      
print(erased_list[k - 1])