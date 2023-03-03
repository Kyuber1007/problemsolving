import sys
import time

input = sys.stdin.readline
N = int(input())
weight_limits = list(map(int, input().split()))
M = int(input())
box_weights = list(map(int, input().split()))

weight_limits.sort(reverse=True)
box_weights.sort(reverse=True)

time_ = 0


if box_weights[0] > weight_limits[0]:
    print(-1)
else:
    time1 = time.time()
    while box_weights:
        if not box_weights:
            break
        for limit in weight_limits:
            for box in box_weights:
                if box <= limit:
                    box_weights.remove(box)
                    break
        time_ += 1
    print(time_)
    time2 = time.time()
    # print(time2 - time1)
