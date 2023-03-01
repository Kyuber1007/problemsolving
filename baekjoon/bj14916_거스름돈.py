import sys

n = int(sys.stdin.readline())

tem_5 = n // 5
tem_2 = (n - tem_5 * 5) // 2

flag = 1

while n != (tem_5 * 5 + tem_2 * 2):
    tem_5 -= 1
    tem_2 = (n - (tem_5 * 5)) // 2
    if tem_5 < 0:
        flag = 0
        break
if flag:
    print(tem_2 + tem_5)
else:
    print(-1)
