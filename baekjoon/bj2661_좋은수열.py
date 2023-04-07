# import sys
# input = sys.stdin.readline

# N = int(input().strip())

# result = []

# def check_possibility():
#     length = len(result)
#     for j in range(1, length//2 + 1):
#         if result[-j:] == result[-2 * j: -j]:
#             return False
#     return True
  
# def dfs(idx):    
#     if idx == N:
#         print(''.join(map(str, result)))
#         exit()
        
#     for i in range(1, 4):
#         result.append(i)
#         if check_possibility():
#             dfs(idx + 1)
#         result.pop()
  
# dfs(0)


import sys
N = int(sys.stdin.readline().strip())
result = []

def check_possibility():
    for j in range(len(result)//2 + 1):
        if result[-j:] == result[-2*j: -j]:
            return False
    return True

def dfs(idx):
    
    if idx == N:
        print(''.join(map(str, result)))
        exit(0)
    
    for i in range(1, 4):
        result.append(i)
        if check_possibility():
            dfs(idx + 1)
        result.pop()
    return

dfs(0)