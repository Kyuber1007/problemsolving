import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(s):
    if len(s) == M:
        for j in range(len(s) - 1): 
            if s[j] > s[j + 1]:
                return
        print(' '.join(map(str, s)))
        return 
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()
dfs([])