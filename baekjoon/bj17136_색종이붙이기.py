# import sys
# input = sys.stdin.readline

# def dfs(x, y, cnt):
#     global result
    
#     if x >= 10:
#         result = min(result, cnt)
#         return
      
#     if y >= 10:
#         dfs(x + 1, 0, cnt)
#         return
      
#     if grids[x][y] == 1:
#         for i in range(5):
#             if papers[i] == 0:
#                 continue
#             if x + i >= 10 or y + i >= 10:
#                 break

#             flag = True
#             for k in range(i + 1):
#                 for l in range(i + 1):
#                     if grids[x + k][y + l] == 0:
#                         flag = False
#                         break
#                 if flag == False:
#                     break
            
#             if flag:
#                 papers[i] -= 1
#                 for k in range(i + 1):
#                     for j in range(i + 1):
#                         grids[x + k][y + j] = 0
#                 dfs(x, y + i + 1, cnt + 1)
#                 papers[i] += 1
#                 for k in range(i + 1):
#                     for j in range(i + 1):
#                         grids[x + k][y + j] = 1
#     else:              
#         dfs(x, y + 1, cnt )
#     return


# grids = [list(map(int, input().split())) for _ in range(10)]
# result = 26
# papers = [5, 5, 5, 5, 5]
# dfs(0, 0, 0)
# print(-1 if result == 26 else result)


import sys
input = sys.stdin.readline

grids = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 0, 0, 0, 0]
result = 26

def dfs(x, y, count):
    global result
    
    # 제일 마지막 row 보다 클 때
    if x >= 10:
        result = min(result, count)
        return 
    # 제일 마지막 col 보다 클 때
    if y >= 10:
        dfs(x + 1, 0, count)
        return

    # 정상적인 경우에서 paper를 놓아야하는 상황이라면
    if grids[x][y] == 1:
        for i in range(5):
            # 남아있는 paper가 없으면 넘어가야함 
            if papers[i] == 5:
                continue
            nx = x + i
            ny = y + i
            
            # 범위를 벗어나면 다음으로 넘어감
            if nx >= 10 or ny >= 10:
                continue
            
            flag = True
            # 해당 종이가 모두 1인 부분을 덮는지 확인
            # 그렇지 않다면 사용할 수 없음
            for j in range(x, nx + 1):
                for k in range(y, ny + 1):
                    if grids[j][k] == 0:
                        flag = False
                        break
                if flag == False:
                    break
            
            if flag:
                papers[i] += 1
                for j in range(x, x + i + 1):
                    for k in range(y, y + i + 1):
                        grids[j][k] = 0
                dfs(x, ny + 1, count + 1)
                papers[i] -= 1
                for j in range(x, x + i + 1):
                    for k in range(y, y + i + 1):
                        grids[j][k] = 1
    else:
        dfs(x, y + 1, count)
    return

dfs(0, 0, 0)

print(-1 if result == 26 else result)