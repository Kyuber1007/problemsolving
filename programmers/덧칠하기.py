def solution(n, m, section):
    answer = 0

    idx = section[0] + m - 1
    answer += 1
    
    for i in range(1, len(section)):
        if section[i] <= idx:
            continue
        else:
            idx = section[i] + m - 1
            answer += 1
            
            
    
            
    return answer