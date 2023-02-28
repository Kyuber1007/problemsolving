import sys
import math
input = sys.stdin.readline
n = int(input())

for i in range(n):
    num = int(input())
    flag = 1
    if num == 0 or num == 1:
        print(2)
    else:
        while True:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0: 
                    flag = 0
                    break
            
            if flag == 1:
                print(num)
                break
            else:
                flag = 1
                num += 1