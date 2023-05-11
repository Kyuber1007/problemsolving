from heapq import heappop, heappush

def solution(k, score):
    answer = []
    
    # 명예의 전당 list
    high_score = []
    
    for i in score:
        # k보다 명예의 전당 갯수가 적으면 일단 추가함
        if len(high_score) < k:
            heappush(high_score, i)
        # k와 같다면 조건을 비교해야함
        else:
            # 제일 적은 점수와 현재 점수를 비교함
            lowest = high_score[0]
            if lowest < i:
                heappop(high_score)
                heappush(high_score, i)
        # 최저 점수를 추가함
        answer.append(high_score[0])
    
    return answer