import sys
input = sys.stdin.readline

N = int(input().strip())
eggs = []
for i in range(N): 
    eggs.append(list(map(int, input().split())))    

max_ = 0

def dfs(idx):
    global max_
    
    if idx == N:
        count = 0
        for egg in eggs:
            if egg[0] <= 0:
                count += 1
        if max_ < count:
            max_ = count
        return

    if eggs[idx][0] <= 0:
        dfs(idx + 1)
        return
    
    all_brokend = True
    for i in range(N):
        if idx == i:
            continue
        if eggs[i][0] <= 0:
            continue
        all_brokend = False
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]
        dfs(idx + 1)
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]
    if all_brokend:
        dfs(N)
dfs(0)
print(max_)