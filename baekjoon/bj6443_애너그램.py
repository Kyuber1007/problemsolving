# import sys
# input = sys.stdin.readline

# N = int(input().strip())

# def dfs(word, visited, result):
#     if len(result) == len(word):
#         print(''.join(result))
#         return
#     for i in visited:
#         if visited[i]:
#             visited[i] -= 1
#             result.append(i)
#             dfs(word, visited, result)
#             visited[i] += 1
#             result.pop()
            
# for i in range(N):
#     word = sorted(list(input().strip()))
#     visited = {}
#     for j in word:
#         if j in visited:
#             visited[j] += 1
#         else:
#             visited[j] = 1
#     dfs(word , visited, [])
    
import sys
input = sys.stdin.readline

def dfs():
    if len(results) == len(word):
        print(''.join(results))
        return
    for j in counts:
        if counts[j] > 0:
            counts[j] -= 1
            results.append(j)
            dfs()
            counts[j] += 1
            results.pop()
    return
  
N = int(input().strip())
for i in range(N):
    word = sorted(list(input().strip()))
    
    counts = {}
    results = []
    for i in word:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    dfs()