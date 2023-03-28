import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(s):
    if len(s) == M:
        print(' '.join(str(numbers[j]) for j in s))
        return
  
    for i in range(N):
        if i not in s:
            s.append(i)
            dfs(s)
            s.pop()

dfs([])

