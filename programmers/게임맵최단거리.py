from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    answer = 0
    length_x = len(maps)
    length_y = len(maps[0])
    visited = [[-1] * length_y for _ in range(length_x)]
    visited[0][0] = 1
    
    q = deque([[0, 0]])
    result = []
    
    while q:
        x, y = q.popleft()
        tem = visited[x][y]
        
        if x == length_x - 1 and y == length_y - 1:
            return tem
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx == length_x or ny == length_y or maps[nx][ny] == 0:
                continue
                
            if visited[nx][ny] > tem + 1 or visited[nx][ny] == -1:
                visited[nx][ny] = tem + 1
                q.append([nx, ny])
    return -1