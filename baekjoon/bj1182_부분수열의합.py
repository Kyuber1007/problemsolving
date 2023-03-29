import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
tem = []

def dfs(n, idx):
    global result
    if len(tem) == n:
        # print(tem)
        value = sum(tem)
        if value == S: 
            result += 1
        return 
    for j in range(idx, N):
        tem.append(nums[j])
        dfs(n, j + 1)
        tem.pop()
        
for i in range(1, N + 1):
    dfs(i, 0)
print(result)