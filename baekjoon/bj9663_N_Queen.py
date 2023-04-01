import sys

def dfs(idx):
    global count
    
    if idx == N:
        count += 1
        return
    
    for i in range(N):
        flag = 1
        if visited[i] == 0:
            for j in range(idx):
                if abs(candidates[j] - i) == abs(j - idx):
                    flag = 0
                    break
            if flag:
                visited[i] = 1
                candidates.append(i)
                dfs(idx + 1)
                visited[i] = 0
                candidates.pop()

N = int(sys.stdin.readline().strip())
count = 0

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    candidates = [i]
    dfs(1)
    
print(count)