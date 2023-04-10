def solution(park, routes):
    answer = []
    x_length = len(park)
    y_length = len(park[0]) 
    
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
    
    for order in routes:
        direction, amount = order.split()
        amount = int(amount)
        flag = True
        
        if direction == 'E':
            ny = y + amount
            if ny >= y_length:
                continue
            for i in range(y, ny + 1):
                if park[x][i] == 'X':
                    flag = False
                    break
            if flag:
                y = ny   
                
        elif direction == 'W':
            ny = y - amount
            if ny < 0:
                continue
            for i in range(ny, y + 1):
                if park[x][i] == 'X':
                    flag = False
                    break
            if flag:
                y = ny    
                
        elif direction == 'N':
            nx = x - amount
            if nx < 0:
                continue
            for i in range(nx, x + 1):
                if park[i][y] == 'X':
                    flag = False
                    break
            if flag:
                x = nx
        elif direction == 'S':
            nx = x + amount
            if nx >= x_length:
                continue
            for i in range(x, nx + 1):
                if park[i][y] == 'X':
                    flag = False
                    break
            if flag:
                x = nx
    return [x, y]