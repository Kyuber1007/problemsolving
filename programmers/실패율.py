from collections import Counter

def solution(N, stages):
    answer = []
    users = len(stages)
    
    # 각 단계에서 막혀있는 사람의 숫자를 셈
    count = list(Counter(stages).items())
    count.sort()
    
    nando = []
    
    # 각 stage의 난도를 셈
    for i in range(len(count)):
        if count[i][0] > N:
            continue
        nando.append([count[i][0], count[i][1]/users])
        users -= count[i][1]
    nando.sort(key=lambda x:x[1], reverse=True)
    
    
    visited = [0] * N
    for i in nando:
        answer.append(i[0])
        visited[i[0] - 1] = 1
    for i in range(N):
        if visited[i] == 0:
            answer.append(i + 1)
        
    return answer