def solution(m, n, puddles):
    answer = 0
    
    map = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0:
                map[i][j] = 1
            if j == 0:
                map[i][j] = 1
    for y, x in puddles:
        map[x-1][y-1] = -1   
        if x == 1:
            for i in range(y,m):
                map[0][i] = 0
        if y == 1:
            for i in range(x,n):
                map[i][0] = 0
        
    for i in range(1, n):
        for j in range(1, m):
            if map[i][j] == -1:
                continue
            
            elif map[i-1][j] == -1:
                map[i][j] = map[i][j-1]
                
            elif map[i][j-1] == -1:
                map[i][j] = map[i-1][j]
            elif map[i-1][j] == -1 and map[i][j-1] == -1:
                map[i][j] = 0
                
            else:
                map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007
                
    for i in range(n):
        print(map[i])
            
    return map[n-1][m-1] % 1000000007