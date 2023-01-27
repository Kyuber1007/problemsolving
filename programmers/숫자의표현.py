def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tem = 0
        start = i
        while tem < n:
            tem += start
            start += 1
        if tem == n:
            answer += 1
    print(answer)
    return answer
  
solution(16)