from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input().strip())

lectures = []


for i in range(N):
    new_lecture = list(map(int, input().split()))
    lectures.append(new_lecture)
lectures.sort()

rooms = []

# 이전 시작한 강의의 종료시간과 다음에 시작하는 강의의 시작 시간을 비교하므로
# 종료시간을 heapq에 넣은 후 비교하면 됨.
heappush(rooms, lectures[0][1])
for i in range(1, N):
    print(rooms)
    if lectures[i][0] < rooms[0]:
        heappush(rooms, lectures[i][1])
    else:
        heappop(rooms)
        heappush(rooms, lectures[i][1])
print(len(rooms))
