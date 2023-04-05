import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global result
    
    if x >= 10:
        result = min(result, cnt)
        return
      
    if y >= 10:
        dfs(x + 1, 0, cnt)
        return
      
    if grids[x][y] == 1:
        for i in range(5):
            if papers[i] == 0:
                continue
            if x + i >= 10 or y + i >= 10:
                break

            flag = True
            for k in range(i + 1):
                for l in range(i + 1):
                    if grids[x + k][y + l] == 0:
                        flag = False
                        break
                if flag == False:
                    break
            
            if flag:
                papers[i] -= 1
                for k in range(i + 1):
                    for j in range(i + 1):
                        grids[x + k][y + j] = 0
                dfs(x, y + i + 1, cnt + 1)
                papers[i] += 1
                for k in range(i + 1):
                    for j in range(i + 1):
                        grids[x + k][y + j] = 1
    else:              
        dfs(x, y + 1, cnt )
    return


grids = [list(map(int, input().split())) for _ in range(10)]
result = 26
papers = [5, 5, 5, 5, 5]
dfs(0, 0, 0)
print(-1 if result == 26 else result)