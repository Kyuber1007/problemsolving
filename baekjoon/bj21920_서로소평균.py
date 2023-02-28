import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
X = int(input())

def GCD(a, b): 
    if b % a == 0: 
        return a
    else:
        return GCD(b % a, a)
sum_ = 0
count = 0

for i in range(N):

    if GCD(X, A[i]) == 1:
        sum_ += A[i]
        count += 1
print(sum_ / count)