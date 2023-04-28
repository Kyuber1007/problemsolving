def solution(routes):
    answer = 0

    routes.sort(key=lambda x: (x[1], x[0]))

    tem = -30001
    for i, values in enumerate(routes):
        if i == 0:
            tem = values[1]
            answer += 1
            continue
        if tem >= values[0]:
            continue
        else:
            tem = values[1]
            answer += 1

    return answer
