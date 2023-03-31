import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grids = []
for i in range(N):
    grids.append(list(map(int, input().split())))

max_ = 0
visited = [[0] * M for _ in range(N)]

def dfs(x, y, sum):
    global max_

    if y == M:
        y = 0
        x += 1
    
    if x == N:
        max_ = max(sum, max_)
        return
      
    # ㄱ 모양
    if y - 1 >= 0 and x + 1 < N and visited[x][y] == 0 and visited[x][y-1] == 0 and visited[x+1][y] == 0:
        visited[x][y] = 1
        visited[x+1][y] = 1
        visited[x][y-1] = 1
        tem = grids[x][y] * 2 + grids[x+1][y] + grids[x][y-1]
        dfs(x, y+1, sum + tem)
        visited[x][y] = 0
        visited[x+1][y] = 0
        visited[x][y-1] = 0
    # ㄱ 을 오른쪽으로 뒤집은 모양
    if x + 1 < N and y + 1 < M and visited[x][y] == 0 and visited[x][y+1] == 0 and visited[x+1][y] == 0:
        visited[x][y] = 1
        visited[x+1][y] = 1
        visited[x][y+1] = 1
        tem = grids[x][y] * 2 + grids[x+1][y] + grids[x][y+1]
        dfs(x, y+1, sum + tem)
        visited[x][y] = 0
        visited[x+1][y] = 0
        visited[x][y+1] = 0
    
    # ㄴ 모양
    if x - 1 >= 0 and y + 1 < M and visited[x][y] == 0 and visited[x][y+1] == 0 and visited[x-1][y] == 0:
        visited[x][y] = 1
        visited[x-1][y] = 1
        visited[x][y+1] = 1
        tem = grids[x][y] * 2 + grids[x-1][y] + grids[x][y+1]
        dfs(x, y + 1, sum + tem)
        visited[x][y] = 0
        visited[x-1][y] = 0
        visited[x][y+1] = 0
    # ㄴ을 오른쪽으로 뒤집은 모습
    if x - 1 >= 0 and y - 1 >= 0 and visited[x][y] == 0 and visited[x][y-1] == 0 and visited[x-1][y] == 0:
        visited[x][y] = 1
        visited[x][y-1] = 1
        visited[x-1][y] = 1
        tem = grids[x][y] * 2 + grids[x-1][y] + grids[x][y-1] 
        dfs(x, y+1, sum + tem)
        visited[x][y] = 0
        visited[x][y-1] = 0
        visited[x-1][y] = 0
    dfs(x, y+1, sum)

dfs(0, 0, 0)
print(max_)