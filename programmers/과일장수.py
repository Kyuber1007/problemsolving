def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    idx = m-1
    for i in range(len(score)//m):
        tem = score[idx]
        answer += tem * m
        idx += m
    return answer