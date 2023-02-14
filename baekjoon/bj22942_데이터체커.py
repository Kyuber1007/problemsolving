import sys
input = sys.stdin.readline
n = int(input())
flag = 1
circles = []

for i in range(n):
    x, r = map(int, input().split())
    circles.append([x-r, i, 0])
    circles.append([x+r, i, 1])
    
circles.sort()
circles_stack = []

for i in range(len(circles)):
    if circles[i][2] == 0:
        circles_stack.append(circles[i])
    else:
        cur_circle = circles_stack.pop()
        if cur_circle[1] != circles[i][1]:
            flag = 0
            print("NO")
            break
if flag == 1:
    print("YES")
    