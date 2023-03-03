import sys
import heapq

input = sys.stdin.readline

N = int(input())

meetings = []

for i in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort()

end_times = []
heapq.heappush(end_times, meetings[0][1])
for i in range(1, N):
    start_time = meetings[i][0]
    end_time = meetings[i][1]
    if start_time < end_times[0]:
        heapq.heappush(end_times, end_time)
    else:
        heapq.heappop(end_times)
        heapq.heappush(end_times, end_time)
print(len(end_times))
