def solution(progresses, speeds):
    answer = []
    index = 0
    while True:
        count = 0
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

        while progresses[index] >= 100:
            index += 1
            count += 1
            if index == len(progresses):
                break
        if count > 0:
            answer.append(count)
        if index == len(progresses):
            break
    return answer


# solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
