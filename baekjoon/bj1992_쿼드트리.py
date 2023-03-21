import sys
input = sys.stdin.readline

N = int(input())
videos = []

for i in range(N):
    videos.append(list(map(int, input().strip())))


answer = ''


def solution(x, y, N):
    cur_ = videos[x][y]
    global answer
    for i in range(x, x + N):
        for j in range(y, y + N):
            if videos[i][j] != cur_:
                cur_ = -1
                break
    if cur_ == -1:
        answer += '('
        solution(x, y, N//2)
        solution(x, y + N//2, N//2)
        solution(x + N//2, y, N//2)
        solution(x + N//2, y + N//2, N//2)
        answer += ')'
    else:
        answer += str(cur_)


solution(0, 0, N)
print(answer)
