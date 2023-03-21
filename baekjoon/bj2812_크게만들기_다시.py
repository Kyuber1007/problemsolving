import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().strip()))

stack = []
count = 0

for number in numbers:
    while stack and stack[-1] < number and count < K:
        stack.pop()
        count += 1
    stack.append(number)

print(''.join(map(str, stack)))
