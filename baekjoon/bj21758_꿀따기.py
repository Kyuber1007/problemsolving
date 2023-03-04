import sys
input = sys.stdin.readline

N = int(input())
places = list(map(int, input().split()))

# 누적합. sum 함수를 이용하면 시간 복잡도 초과
places_sum = [places[0]]
for i in range(1, N):
    places_sum.append(places_sum[i - 1] + places[i])

# 벌 꿀 벌
answer1 = 0
for i in range(1, N - 1):
    answer1 = max(answer1, places_sum[-2] - places[0] + places[i])

# 벌 벌 꿀
for i in range(1, N - 1):
    answer1 = max(answer1, places_sum[-1] * 2 - places[i] -
                  places[0] - places_sum[i])

# 꿀 벌 벌
for i in range(1, N - 1):
    answer1 = max(answer1, places_sum[i - 1] +
                  places_sum[-1] - places[i] - places[-1])

print(answer1)
