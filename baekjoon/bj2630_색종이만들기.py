import sys
input = sys.stdin.readline


def solution(x, y, N):
    global blue_cnt, white_cnt
    color = papers[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if papers[i][j] != color:
                solution(x, y, N//2)
                solution(x, y + N // 2, N//2)
                solution(x + N // 2, y, N//2)
                solution(x + N // 2, y + N // 2, N//2)
                return
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


N = int(input())

papers = []
for i in range(N):
    papers.append(list(map(int, input().split())))
blue_cnt = 0
white_cnt = 0
solution(0, 0, N)

print(white_cnt)
print(blue_cnt)
