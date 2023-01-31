import math


def solution(n):
    answer = 0

    # 2가 들어갈 수 있는 갯수를 찾음.
    tem = n // 2

    # 전부 1로 바뀌기 전까지 가능한 case들을 추가하고, 전부 1로 바뀌었을 땐 1가지 케이스 추가
    while tem >= 0:
        # 맨 처음, 즉, 2가 최대일 경우에 구하는 방법
        if tem == n//2:
            # 2의 배수 일 때
            if n % 2 == 0:
                answer += 1
            # 2의 배수가 아닐 때
            else:
                answer += tem + 1

        # 모두 1일 때 구하는 방법
        elif tem == 0:
            answer += 1

        # 증간 케이스
        else:
            tem1 = n - tem * 2
            answer += int(math.factorial(tem1 + tem) //
                          (math.factorial(tem1) * math.factorial(tem)))
        tem -= 1
    return answer % 1234567


solution(2000)
