import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())

days = 0
populations = []

for i in range(N):
    populations.append(list(map(int, input().split())))


print(populations)
