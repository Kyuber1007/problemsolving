import sys

input = sys.stdin.readline

m = int(input())
n = int(input())

num_list = []
for num in range(m, n + 1):
    flag = 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = 0
                break
    else:
        flag = 0
    
    if flag == 1:
        num_list.append(num)
      
if num_list:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)