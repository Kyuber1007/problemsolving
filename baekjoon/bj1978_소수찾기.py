import sys

n = int(sys.stdin.readline())
numbers = (map(int, sys.stdin.readline().split()))

count = 0
for num in numbers:
    flag = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = 1
                break
    else:
        flag = 1  
    if flag == 0:
        count += 1
        
print(count)