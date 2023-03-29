import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grids = [[0] * (M + 1) for _ in range(N + 1)]

count = 0

def dfs(x, y):
    global count
    
    if y == M + 1:
        y = 1
        x += 1
        if x == N + 1:
            count += 1
            return
          
    dfs(x, y + 1)
    
    if not (grids[x-1][y] == 1 and grids[x-1][y-1] == 1 and grids[x][y-1] == 1):
        grids[x][y] = 1
        dfs(x, y + 1)
        grids[x][y] = 0
    
dfs(1, 1)
print(count)