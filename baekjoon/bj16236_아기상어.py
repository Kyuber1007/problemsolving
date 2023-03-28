import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())

grids = []
cur_x, cur_y = -1, -1

for i in range(N):
    new_row = list(map(int, input().split()))
    grids.append(new_row)
    if cur_x == -1:
        for j in range(len(new_row)):
            if new_row[j] == 9:
                cur_x = i
                cur_y = j

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(x, y, size):
    q = deque()
    tem = []
    
    q.append([x, y, 0])
    visited = [[0] * N for _ in range(N)]
    distance = 0
    
    while q:
        cur_x, cur_y, cur_dist = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 범위 내에 있고 아직 방문하지 않은 구간일 때
            if  0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 방문했다고 표시
                visited[nx][ny] = 1
                
                # 지나갈 수 있는 자리인지 파악
                if grids[nx][ny] <= cur_size:
                    # 지나갈 수 있으면 queue에 넣고
                    q.append([nx, ny, cur_dist + 1])
                    # 먹을 수 있으면 후보에 넣음
                    if grids[nx][ny] < cur_size and grids[nx][ny] != 0:
                        tem.append([[nx, ny], cur_dist + 1])
    tem.sort(key=lambda x: (x[1], x[0][0], x[0][1]))
    return tem

result = 0
cur_size = 2
size_count = 0
while True:
    candidates = bfs(cur_x, cur_y, cur_size)
    if len(candidates) == 0:
        break
    next_x, next_y = candidates[0][0]
    result += candidates[0][1]

    grids[cur_x][cur_y] = 0
    grids[next_x][next_y] = 9
    cur_x = next_x
    cur_y = next_y
    
    size_count += 1
    if size_count == cur_size:
        cur_size += 1
        size_count = 0
    
    if cur_size >= 7:
        cur_size = 7
 
print(result)