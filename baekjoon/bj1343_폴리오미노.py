import sys
boards = sys.stdin.readline().strip().split(".")

answer = ""
flag = 1

for board in boards:
    if len(board) % 2 != 0:
        flag = 0
        break
    else:
        length = len(board)

        tem_A = length // 4
        tem_B = length % 4
        answer += 'AAAA' * tem_A
        answer += 'B' * tem_B
    answer += '.'

if flag:
    print(answer[:-1])
else:
    print(-1)
