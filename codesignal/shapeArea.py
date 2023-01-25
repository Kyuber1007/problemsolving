def solution(n):
    add = 0 
    for i in range(n):
        add += 2 * (i + 1 ) - 1
        if i == n - 2:
            add *= 2 
    return add