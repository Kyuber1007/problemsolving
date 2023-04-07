# import sys

# n = int(sys.stdin.readline())

# tem_5 = n // 5
# tem_2 = (n - tem_5 * 5) // 2

# flag = 1

# while n != (tem_5 * 5 + tem_2 * 2):
#     tem_5 -= 1
#     tem_2 = (n - (tem_5 * 5)) // 2
#     if tem_5 < 0:
#         flag = 0
#         break
# if flag:
#     print(tem_2 + tem_5)
# else:
#     print(-1)


import sys
input = sys.stdin.readline

n = int(input().strip())
answer = 0

num_5 = n // 5
num_2 = (n - (5*num_5)) // 2

# print(num_5, num_2)

while num_5 >= 0:
    if num_5 * 5 + num_2 * 2 != n:
        num_5 -= 1
        num_2 = (n - (5*num_5)) // 2
        # print(num_5, num_2)
    else:
        answer = 1
        break
print(-1 if answer == 0 else num_2 + num_5)
