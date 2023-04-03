import sys
input = sys.stdin.readline

grids = [list(map(int, input().split())) for _ in range(9)]
blanks = []

for i in range(9):
    for j in range(9):
        if grids[i][j] == 0:
            blanks.append([i, j])

def check_row(x, y, i):
    for j in range(9):
        if grids[x][j] == i:
            return False
    return True
  
def check_col(x, y, i):
    for j in range(9):
        if grids[j][y] == i:
            return False
    return True
  
def check_square(x, y, i):
    deep_x = (x // 3) * 3
    deep_y = (y // 3) * 3
    
    for j in range(deep_x, deep_x + 3):
        for k in range(deep_y, deep_y + 3):
            if grids[j][k] == i:
                return False
    return True

def dfs(idx):
    if idx == len(blanks):
        for i in range(9):
            print(*grids[i])
        exit(0)
      
    for i in range(1, 10):
        x, y = blanks[idx]
        
        if check_row(x, y, i) and check_col(x, y, i) and check_square(x, y, i):
            grids[x][y] = i
            dfs(idx + 1)
            grids[x][y] = 0
  
dfs(0)