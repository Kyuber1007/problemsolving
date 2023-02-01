def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    while s != 0:
        tem = s//n
        answer.append(tem)
        s -= tem
        n -= 1
    return answer


solution(2, 9)
