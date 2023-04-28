from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0

    # heap으로 만들고
    heapify(scoville)

    # 한개보다 많을 경우 반복함
    while len(scoville) > 1:
        tem = heappop(scoville)

        # 최소값이 K보다 클 때 return answer
        if tem >= K:
            return answer

        # 아닐 경우 더 매운 것을 생산해야함
        else:
            tem2 = heappop(scoville)
            heappush(scoville, tem + tem2*2)
            answer += 1

    if scoville[0] < K:
        return -1

    return answer
