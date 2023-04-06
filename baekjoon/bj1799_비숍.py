import sys
input = sys.stdin.readline

N = int(input().strip())
grids = []
for i in range(N):
    grids.append(list(map(int, input().split())))
