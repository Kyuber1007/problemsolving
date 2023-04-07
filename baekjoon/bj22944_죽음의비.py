import sys
from collections import deque

input = sys.stdin.readline

N, H, D = map(int, input().split())
grids = [list(map(int, input().split())) for i in range(N)]

x, y = 0, 0
for i in range(N):
    for j in range(N):
        if grids[i][j] == 'S':
            x = i
            y = j

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

umbrella = False
umbrella_life = 0
count = 0

def dfs(x, y):
    global count, umbrella, umbrella_life
    q = 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or ny >=  N or nx < 0 or ny < 0:
            return
        else:
            count += 1
            next_place = grids[nx][ny]
            
            if next_place == '.':
                if umbrella:
                    umbrella_life -= 1
                    if umbrella_life == 0:
                        umbrella = False
                else:

    return
  
  
dfs(x, y)