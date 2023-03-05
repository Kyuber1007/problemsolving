import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().strip()))

stack = []
count = 0

for num in numbers:
    while stack and stack[-1] < num and count < K:
        count += 1
        stack.pop()
    stack.append(num)

print(''.join(map(str, stack[:N-K])))
