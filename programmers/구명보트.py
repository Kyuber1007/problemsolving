def solution1(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1

    while i <= j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1
    return answer


solution1([70, 50, 80], 100)

def solution(people, limit):
    answer = 0
    
    people.sort()
    visited = [0] * len(people)
    j = 0
    for i in range(len(people)-1, -1, -1):
        if visited[i] == 1:
            continue
        else:
            tem = people[i]
            
            if tem + people[j] <= limit:
                visited[j] = 1
                j += 1
            visited[i] = 1
            answer += 1
    return answer