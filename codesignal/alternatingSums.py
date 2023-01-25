def solution(a):
    result = [0,0]
    for i, n in enumerate(a):
        if i % 2 == 1:
            result[1] += n
        else:
            result[0] += n
            
    return result
