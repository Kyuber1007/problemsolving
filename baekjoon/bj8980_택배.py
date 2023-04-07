import sys

input = sys.stdin.readline
N, C = map(int, input().split())
M = int(input().strip())

boxes = [list(map(int, input().split())) for _ in range(M)]

# 도착지를 기준으로 정렬
boxes.sort(key=lambda x: x[1])
in_truck = [0] * (N + 1)

count = 0

# 모든 박스를 싯는 경우를 살펴보면서
for s, a, l in boxes:
    tem = l

    # 마을을 지날 때, 각 마을을 최대로 지나도록 함.
    for i in range(s, a):
        if in_truck[i] + tem >= C:
            tem = C - in_truck[i]
    for i in range(s, a):
        in_truck[i] += tem
    count += tem
print(count)
