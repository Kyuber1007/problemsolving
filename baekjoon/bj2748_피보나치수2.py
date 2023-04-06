import sys
input = sys.stdin.readline

n = int(input().strip())

if n == 0:
    print(0)
    exit()

elif n == 1:
    print(1)
    exit()
else:
    tem1 = 0
    tem2 = 1
    for i in range(n):
        tem1 = tem1 + tem2
        tem3 = tem1
        tem1 = tem2
        tem2 = tem3
    print(tem1)