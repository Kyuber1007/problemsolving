import sys
input = sys.stdin.readline

N = int(input())
places = list(map(int, input().split()))
places_sum = sum(places)

# 벌 꿀 벌
answer1 = 0
for i in range(1, N - 1):
    answer1 = max(answer1, places_sum - places[0] - places[-1] + places[i])

# 벌 벌 꿀
for i in range(1, N - 1):
    answer1 = max(answer1, places_sum -
                  places[0] - places[i] + sum(places[i+1:]))

# 꿀 벌 벌
for i in range(1, N - 1):
    answer1 = max(answer1, places_sum -
                  places[-1] - places[i] + sum(places[:i]))

print(answer1)
