from collections import deque

# deque의 rotate 함수를 잘 활용하면 쉽게 해결할 수 있는 문제.
# collections의 전체 개념에 대해서 살펴볼 필요가 있음.
n = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))
s = ""

for i in range(n):
    index, target = balloons.popleft()
    s += str(index) + " "
    if target > 0:
        balloons.rotate(-(target - 1))
    else:
        balloons.rotate(-target)
print(s)
