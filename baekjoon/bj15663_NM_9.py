import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = set()
tem = []

def dfs():
    if len(tem) == M:
        new_str = ' '.join(str(nums[i]) for i in tem)
        if new_str in result:
            return
        else:
            result.add(new_str)
            print(' '.join(str(nums[i]) for i in tem))
            return
    for i in range(N):
        tem_set = set(tem)
        if i not in tem_set:
            tem.append(i)
            dfs()
            tem.pop()
dfs()