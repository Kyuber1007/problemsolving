def solution(priorities, location):
    answer = 1
    priority = priorities[location]
    priorities[location] = -1

    while True:
        max_num = max(priorities)
        if max_num > priority:
            index = priorities.index(max_num)
            priorities = priorities[index + 1:] + priorities[:index]
            answer += 1

        elif max_num == priority:
            if priorities.index(-1) < priorities.index(max_num):
                return answer
            else:
                index = priorities.index(max_num)
                priorities = priorities[index + 1:] + priorities[:index]
                answer += 1
        else:
            return answer


solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)
