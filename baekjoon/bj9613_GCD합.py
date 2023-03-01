import sys

input = sys.stdin.readline

t = int(input())

def GCD(a, b):
    if b % a == 0:
        return a
    else:
        return GCD(b % a, a)

for i in range(t):
    test_case = list(map(int, input().split()))
    sum_value = 0
    
    for j in range(1, test_case[0]):
        for k in range(j + 1, test_case[0] + 1):
            sum_value += GCD(test_case[j], test_case[k])
    print(sum_value)