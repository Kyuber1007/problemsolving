import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
preferences = []

for i in range(N):
    preferences.append(list(map(int, input().split())))

max_value = 0
for i in itertools.combinations(range(M), 3):
    a, b, c = map(int, i)
    max_ = []
    for j in range(N):
        max_.append(
            max(preferences[j][a], preferences[j][b], preferences[j][c]))
    tem = sum(max_)
    if tem > max_value:
        max_value = tem
print(max_value)
