import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    else:
        tem = M - N
        tem2 = 1
        for j in range(M, tem, -1):
            tem2 *= j
        tem3 = 1
        for j in range(1, N + 1):
            tem3 *= j
        print(int(tem2/tem3))