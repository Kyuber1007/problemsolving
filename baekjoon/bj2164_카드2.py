# 1
# import collections
n = int(input())

# deque = collections.deque([i for i in range(1, n + 1)])

# while len(deque) > 1:
#     deque.popleft()
#     deque.append(deque.popleft())

# print(deque[0])

# 2
two_square = 2
if n == 1:
    print(1)

if n > 1:
    while n > two_square:
        two_square *= 2

    print((n-two_square//2) * 2)
