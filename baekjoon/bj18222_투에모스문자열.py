import sys
input = sys.stdin.readline

k = int(input())

cnt = 0


def solution(k):
    tem = 1
    global cnt
    while k - tem >= 0:
        tem *= 2

    if k == 0:
        if cnt % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        k = k - tem//2
        cnt += 1
        solution(k)


solution(k - 1)
