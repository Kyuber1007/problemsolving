import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(s):
    if len(s) == M:
        print(' '.join(str(nums[i]) for i in s))
        return    
      
    for i in range(N):
        s.append(i)
        dfs(s)
        s.pop()
  
  
dfs([])