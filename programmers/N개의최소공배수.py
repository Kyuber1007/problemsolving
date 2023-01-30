# 최소공배수 구하는 함수
def lcm(a, b):
    print(a, b)
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


def solution(arr):
    arr.sort()
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
        print(answer)
    return answer


solution([2, 6, 8, 14])
