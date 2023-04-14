def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        if total % i == 0:
            j = total / i
            if brown == (j * 2 + (i - 2)*2):
                return [int(j), i]
    return answer


def solution2(brown, yellow):
    x = yellow
    y = 1
    
    while x >= y:
        tem = 2 * (x + y + 2)
        
        if tem == brown:
            return [x + 2, y + 2]
        
        y += 1
        while yellow % y != 0:
            y += 1
        x = yellow // y
