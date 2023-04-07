import sys
input = sys.stdin.readline

T = map(str, input().strip())
N = int(input().strip())

textbooks = []

for i in range(N):
    price, name = map(str, input().split())
    textbooks.append([int(price), name])


