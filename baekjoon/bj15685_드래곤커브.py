import sys
input = sys.stdin.readline

N = int(input().strip())

grids = [[0] * 101 for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def generate_new_branch(arr):
    new_branch_shape = [[0, 0]]
    
    for i in range(1, len(arr)):
        pre_x, pre_y = arr[i-1]
        x, y = arr[i]
        
        # 이전 것보다 왼쪽에 있을 때
        if pre_x - x == 0 and pre_y - y == 1:
            new_branch_shape.append([new_branch_shape[i-1][0] - 1, new_branch_shape[i-1][1]])

        # 이전 것보다 오른쪽에 있을 때
        elif pre_x - x == 0 and pre_y - y == -1:
            new_branch_shape.append([new_branch_shape[i-1][0] + 1, new_branch_shape[i-1][1]])

        # 이전 것보다 위에 있을 때
        elif pre_x - x == 1 and pre_y - y == 0:
            new_branch_shape.append([new_branch_shape[i-1][0], new_branch_shape[i-1][1] + 1])
        
        # 이전 것보다 아래에 있을 때
        elif pre_x - x == -1 and pre_y - y == 0:
            new_branch_shape.append([new_branch_shape[i-1][0], new_branch_shape[i-1][1] - 1])
    
    new_branch_shape = new_branch_shape[::-1]
    
    new_x, new_y = new_branch_shape[0]
    pre_end_x, pre_end_y = arr[-1]
    
    diff_x = pre_end_x - new_x
    diff_y = pre_end_y - new_y
    
    for i in range(len(new_branch_shape)):
        new_branch_shape[i][0] = new_branch_shape[i][0] + diff_x
        new_branch_shape[i][1] = new_branch_shape[i][1] + diff_y
    return arr[:] + new_branch_shape[1:]
  
  
for i in range(N):
    y, x, d, g = map(int, input().split())
    # 0세대
    branch = [[x, y], [x + dx[d], y + dy[d]]]
    count = 0
    
    while g > 0:
        count += 1
        branch = generate_new_branch(branch)
        g -= 1
    for i in range(len(branch)):
        x, y = branch[i]
        grids[x][y] = 1

result = 0
for i in range(0, len(grids) -1):
    for j in range(0, len(grids)-1):
        if grids[i][j] == 1 and grids[i][j + 1] == 1 and grids[i+1][j] == 1 and grids[i+1][j+1]==1:
            result += 1
print(result)