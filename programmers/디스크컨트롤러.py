from heapq import heappush, heappop


def solution(jobs):
    idx = 0
    q = []
    start = -1
    cur_time, total, length = 0, 0, len(jobs)

    while idx < length:
        for i in range(length):
            if start < jobs[i][0] <= cur_time:
                heappush(q, [jobs[i][1], jobs[i][0]])
        if q:
            cur_job = heappop(q)
            start = cur_time

            total += cur_time + cur_job[0] - cur_job[1]
            cur_time += cur_job[0]
            idx += 1
        else:
            cur_time += 1
    return total // length
