def solution(prices):
    answer = []
    
    length = len(prices)
    
    # 가질 수 있는 최대값으로 설정
    answer = [i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range(1, length):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer