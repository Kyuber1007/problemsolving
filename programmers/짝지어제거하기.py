def solution(s):
    answer = -1
    count = 0
    stack = []
    
    stack.append(s[0])
    for i in range(1, len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
                continue
        stack.append(s[i])
    return 0 if stack else 1