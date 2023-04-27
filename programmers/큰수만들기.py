def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -=1
        stack.append(i)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)