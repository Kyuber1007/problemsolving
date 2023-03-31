import sys
from heapq import heappush, heappop


input = sys.stdin.readline


C = int(input().strip())

def dfs(arr, idx, sum, max_, startings, positions, max_list):
    if idx == 11:
        heappush(max_list, sum)
        heappop(max_list)
        return max_
    
    if idx in startings:
        dfs(arr, idx + 1, sum, max_, startings, positions, max_list)
        
    for i in range(11): 
        if arr[idx][i] != 0 and positions[i] != 1:
            startings.add(idx)
            sum += arr[idx][i]
            positions[i] = 1
            dfs(arr, idx + 1, sum, max_, startings, positions, max_list)
            startings.discard(idx)
            positions[i] = 0
            sum -= arr[idx][i]
    return
  
def solve_problem(cases):
    max_ = 0
    startings = set()
    positions = [0] * 11
    maxs_list = [0]
    dfs(cases, 0, 0, 0, startings, positions, maxs_list)
    print(heappop(maxs_list))
    return


for i in range(C):
    cases = []
    for i in range(11): 
        cases.append(list(map(int, input().split())))
    solve_problem(cases)