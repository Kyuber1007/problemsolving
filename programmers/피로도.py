answer = -1
def solution(k, dungeons):
    # 던전 경우의 수를 위해서 방문했는지 확인하는 배열
    visited = [0] * len(dungeons)
    
    # 현재 가고자 하는 경로
    routes = []
    def dfs():
        global answer
        
        # route가 있을 때 미리미리 확인하는 경로, 불가능하면 그 뒤에를 테스트할 필요가 없음
        if len(routes) > 0:
            print(routes)
            tem = k
            for j in range(len(routes)):
                if tem < dungeons[routes[j]][0]:
                    return
                else:
                    tem -=  dungeons[routes[j]][1]
            answer = max(answer, len(routes))
                
        for i in range(len(dungeons)):
            if visited[i] == 0:
                visited[i] = 1
                routes.append(i)
                dfs()
                visited[i] = 0
                routes.pop()
    dfs()
    return answer