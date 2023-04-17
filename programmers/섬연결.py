def solution(n, costs):
    answer = 0
    in_comm = set([costs[0][0]])
    costs.sort(key=lambda x:x[2])
    
    while len(in_comm) < n:
        for i in range(len(costs)):
            a, b, cost =  costs[i]
            if a in in_comm and b in in_comm:
                continue
            if a in in_comm or b in in_comm:
                answer += cost
                in_comm.add(a)
                in_comm.add(b)
                break
        print(in_comm)
    return answer
solution(	4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
