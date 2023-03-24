import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())

populations = []
for i in range(N):
    populations.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    tem = []
    q.append((i, j))
    tem.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range (4):       
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(populations[x][y] - populations[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    tem.append((nx, ny))
    return tem

days = 0
while True:
    unchanged = True
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                opened = bfs(i, j)
                
            if len(opened) > 1:    
                value = sum(populations[x][y] for x, y in opened) // len(opened)
                for x, y, in opened:
                    populations[x][y] = value
                unchanged = False
    if unchanged:
        break
    days += 1
print(days)