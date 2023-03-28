import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()


def dfs(s):
    if len(s) == M:
        print(' '.join(str(numbers[j]) for j in s))
        return

    for i in range(N): 
        if len(s) > 0:
            if s[-1] < i:
                s.append(i)
                dfs(s)
                s.pop()

        else:
            s.append(i)
            dfs(s)
            s.pop()
dfs([])