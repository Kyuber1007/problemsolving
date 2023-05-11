def solution(food):
    answer = ''
    tem = ''
    
    for i in range(1, len(food)):
        tem += str(i) * (food[i] // 2)
    answer = tem + '0' + ''.join(tem[::-1])
    return answer