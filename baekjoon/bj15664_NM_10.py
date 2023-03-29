import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = set()

tem = []
def dfs(idx):
    if len(tem) == M:
        new_str = ' '.join(str(nums[i]) for i in tem)
        if new_str in result:
            return
        else:
            result.add(new_str)
            print(' '.join(str(nums[i]) for i in tem))
            return
    
    if N - idx < M - len(tem):
        return
    
    for i in range(idx, N):
        tem.append(i)
        dfs(i + 1)
        tem.pop()

dfs(0)