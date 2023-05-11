def solution(s):
    answer = []
    s = s[2:-2]
    tem = s.split('},{')
    tem.sort(key=len)
    
    for i in range(len(tem)):
        _ = tem[i].split(',')
        for j in _:
            if int(j) not in answer:
                answer.append(int(j))
    return answer