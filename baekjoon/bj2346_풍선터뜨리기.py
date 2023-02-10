from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))

print(balloons)
s = ""
for i in range(n):
    index, target = balloons.popleft()
    print(index, target)
    s += str(index) + " "

    balloons.rotate(target)
print(s)
