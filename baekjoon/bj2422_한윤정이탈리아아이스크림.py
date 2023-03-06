import sys
import itertools

input = sys.stdin.readline
N, M = map(int, input().split())

ice_creams = [[True for i in range(N)] for j in range(N)]

for i in range(M):
    limit_a, limit_b = map(int, input().split())
    ice_creams[limit_a - 1][limit_b-1] = False
    ice_creams[limit_b-1][limit_a-1] = False

count = 0
for i in itertools.combinations(range(N), 3):
    a, b, c = i[0], i[1], i[2]
    if ice_creams[a][b] and ice_creams[a][c] and ice_creams[b][c]:
        count += 1

print(count)
