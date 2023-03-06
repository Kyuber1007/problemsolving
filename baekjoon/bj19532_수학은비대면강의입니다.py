import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

x = int((c*e - f*b) / (a*e - b*d))
y = int((c*d - f*a) / (b*d - a*e))


print(x, y)
