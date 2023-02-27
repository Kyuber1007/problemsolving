import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())

problems = {}

min_difficulties = []
max_difficulties = []

for _ in range(n):
    new_ = input().split()
    problems[new_[0]] = int(new_[1])
    heappush(min_difficulties, (int(new_[1]), new_[0]))
    heappush(max_difficulties, (int(new_[1]) * -1, new_[0]))
    
m = int(input())

def organize_heap(heap, key = 1):
    values = problems.values()
    for i in range(len(heap)):
        if heap[i][0] not in values:
            heap


for _ in range(m):
    operation = input().split()
    if operation[0]== 'add':
        problems[operation[1]] = int(operation[2])
        heappush(min_difficulties, (int(operation[2]), operation[1]))
        heappush(max_difficulties, (int(operation[2]) * -1, operation[1]))
        
    elif operation[0]=='recommend':
        if operation[1] == '1':
            organize_heap(max_difficulties)
            max_ = heappop(max_difficulties)
            print(max_[1])
        else:
            organize_heap(min_difficulties)
            min_ = heappop(min_difficulties)
            print(min_[1])
            
    elif operation[0] == 'solved':
        num = problems.pop(operation[1])