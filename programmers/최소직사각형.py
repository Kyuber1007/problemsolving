def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            tem = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = tem
    max_x = 0
    max_y = 0
    
    for _ in sizes:
        if _[0] > max_x:
            max_x = _[0]
        if _[1] > max_y:
            max_y = _[1]
    return max_x * max_y