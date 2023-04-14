def solution(array, commands):
    answer = []
    tem = []
    for cur in commands:
        tem = array[cur[0]-1:cur[1]]
        tem.sort()
        answer.append(tem[cur[2] -1])
    return answer