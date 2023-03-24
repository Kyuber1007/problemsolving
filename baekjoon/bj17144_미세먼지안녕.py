import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

grids = []
cleaners = []
cleaner_count = 0
for i in range(R):
    row = list(map(int, input().split()))
    if cleaner_count == 0:
        for j in range(len(row)):
            if row[j] == -1:
                cleaner_count += 1
                cleaners.append([i,j])
                cleaners.append([i + 1, j])
    grids.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


while T > 0:
    T -= 1
    new_grids = [[0] * C for _ in range(R)]
    for i in range(2):
        new_grids[cleaners[i][0]][cleaners[i][1]] = -1
    # step1: 미세먼지 확산
    for x in range(len(grids)):
        for y in range(len(grids[i])):
            cur_dust = grids[x][y]
            if cur_dust != -1:
                spread_count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and grids[nx][ny] != -1:
                        spread_count += 1
                        new_grids[nx][ny] += cur_dust // 5
                new_grids[x][y] += (grids[x][y] - (cur_dust//5) * spread_count)                
    grids = new_grids
    # for grid in grids:
    #     print(grid)

    # step2: 공기적정기 작동
    # 밀어내는게 아니라 공기청정기 쪽으로 끌어오는 방향으로 구현.
    for i in range(len(cleaners)):
        x, y = cleaners[i][0], cleaners[i][1]
        tem_x = x
        tem_y = y
        # print(i, tem_x, tem_y)
        
        # 최좌측으로 가면서 왼쪽 값을 오른쪽으로 옮김 (공기청정기로 빨려들어가도록)
        while tem_y > 0:
            tem_y -= 1
            grids[tem_x][tem_y] = grids[tem_x][tem_y - 1]
        # print(i, tem_x, tem_y)
        
        
        # 위의 공기청정기일 때, 최상단으로 올라가면서, 위의 값을 아래로 옮김.
        if i == 0:
            while tem_x > 0:
                grids[tem_x][tem_y] = grids[tem_x - 1][tem_y] 
                tem_x -= 1
        # 아래 공기청정기일 때, 최하단을 내려가면서, 아래의 값을 위로 옮김.ㄴ        
        else:
            while tem_x < R - 1:
                grids[tem_x][tem_y] = grids[tem_x + 1][tem_y]
                tem_x += 1
                
        # print(i, tem_x, tem_y)
        
        # 최우측으로 가면서 우측의 값을 좌측으로 옮김
        while tem_y < C - 1:
            grids[tem_x][tem_y] = grids[tem_x][tem_y + 1]
            tem_y += 1
        # print(i, tem_x, tem_y)
        
        # 위의 공기청정기 일 때, x값까지 내려오면서, 아래의 값을 위로 옮김
        if i == 0:
            while tem_x < x:
                grids[tem_x][tem_y] =  grids[tem_x + 1][tem_y]
                tem_x += 1
        # 아래 공기정정기 일 때, x값까지 올라가며, 위의 값을 아래로 내림
        else:
            while tem_x > x:
                grids[tem_x][tem_y] = grids[tem_x - 1][tem_y]
                tem_x -= 1
                
        # 공기청정기 y의 위치까지 좌측으로 이동하며 좌측의 값을 우측으로 옮김
        while tem_y > y + 1:
            grids[tem_x][tem_y] = grids[tem_x][tem_y - 1]
            tem_y -= 1
        grids[tem_x][tem_y] = 0
        grids[x][y] = -1
        # for grid in grids:
        #     print(grid)        
result = 0
for i in range(len(grids)):
    result += sum(grids[i])
print(result + 2)