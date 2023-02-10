import sys
import collections

n = int(sys.stdin.readline())

deque = collections.deque([])

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push_back':
        deque.append(order[1])
    elif order[0] == 'push_front':
        deque.appendleft(order[1])
    elif order[0] == 'size':
        print(len(deque))
    elif order[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(deque) == 0:
            print(-1)
            continue
        if order[0] == 'pop_front':
            print(deque.popleft())
        elif order[0] == 'pop_back':
            print(deque.pop())

        elif order[0] == 'front':
            print(deque[0])
        elif order[0] == 'back':
            print(deque[-1])
