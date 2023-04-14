def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n = len(citations)
    
    for i in range(n):
        if i >= citations[i]:
            return i
    return n
    
