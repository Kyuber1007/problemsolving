def solution(n):
    fibo = [1, 1]
    for i in range(2, n):
        fibo.append((fibo[i - 1] + fibo[i - 2]) % 1234567) 
    return fibo[-1]
    
solution(100)