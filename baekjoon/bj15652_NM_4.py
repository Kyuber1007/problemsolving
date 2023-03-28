import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(s):
    if len(s) == M:
        
        print(' '.join(map(str, s)))
        return
      
    for i in range(1, N + 1):
        s.append(i)
        if len(s) > 1:
            if s[-1] >= s[-2]:
                dfs(s)
        else:
            dfs(s)
        s.pop()
  
dfs([])