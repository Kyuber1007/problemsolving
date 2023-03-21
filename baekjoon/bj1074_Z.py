import sys
input = sys.stdin.readline


def solution(x, y, n):
    global count


N, r, c = map(int, input().split())
count = 0

total_size = 2**(2 * N - 2)
print(total_size)

solution(0, 0, total_size)
print(count)
