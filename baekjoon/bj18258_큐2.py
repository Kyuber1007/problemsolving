import collections
import sys

n = int(sys.stdin.readline())
deque = collections.deque([])

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        deque.append(order[1])
    elif order[0] == 'pop':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif order[0] == 'size':
        print(len(deque))
    elif order[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif order[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
