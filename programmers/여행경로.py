answer = []

def solution(tickets):
    tickets_num = len(tickets)
    visited = [0] * tickets_num
    candidate = ['ICN']

    # 모든 극한까지 가보면서, 끝에 가는 경우를 구함
    # visited로 사용한 ticket을 골라냄
    def dfs():
        if sum(visited) == tickets_num:
            answer.append(candidate[:])
            return
        for i in range(len(tickets)):
            if visited[i] == 0 and candidate[-1] == tickets[i][0]:
                candidate.append(tickets[i][1])
                visited[i] = 1
                dfs()
                candidate.pop()
                visited[i] = 0
        return
    dfs()
    
    answer.sort()
    return answer[0]