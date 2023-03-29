import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def dfs(s):
    if len(s) == M:
        print(' '.join(str(nums[i]) for i in s))
        return
    for i in range(N):
        if len(s) > 0:
            if s[-1] <= i:
                s.append(i)
                dfs(s)
                s.pop()
        else:
            s.append(i)
            dfs(s)
            s.pop()

    return

dfs([])
