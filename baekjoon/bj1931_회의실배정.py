import sys

input = sys.stdin.readline

N = int(input().strip())
meetings = []

for i in range(N):
    new_meeting = tuple(map(int, input().split()))
    meetings.append(new_meeting)

# 종료 시점 기준으로 비교를 할거임. 그래서 시작시간 기준으로 정렬한 후, 종료 시간 기준으로 정렬함.
# 종료 시간이 작은 순 -> 종료 시간이 같다면 시작 시간이 작은 순으로 정렬.
meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

result = 1
for i, meeting in enumerate(meetings):
    if i == 0:
        prev_end = meetings[i][1]
    elif meeting[0] >= prev_end:
        prev_end = meeting[1]
        result += 1

print(result)
