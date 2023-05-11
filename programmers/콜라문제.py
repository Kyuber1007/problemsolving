def solution(a, b, n):
    answer = 0
    
    while n >= a:
        tem = n // a
        n -= tem * a
        n += tem * b
        answer += tem * b
        
    return answer