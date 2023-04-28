def solution(n, computers):
    count = 0
    length = len(computers)
    next = []

    for i in range(length):
        next.append(i)
        tem = []
        while len(next) != 0:
            next_index = next.pop()
            for j in range(length):
                if computers[next_index][j] == 1:
                    next.append(j)
                    computers[next_index][j] = 0
                    computers[j][next_index] = 0
                    tem.append(j)
        if tem != []:
            count += 1
    return count


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
