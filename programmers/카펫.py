def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        if total % i == 0:
            j = total / i
            if brown == (j * 2 + (i - 2)*2):
                return [int(j), i]
    return answer


solution(10, 2)
