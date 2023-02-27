import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

# 최대공약수를 구함.
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)  
greatest = gcd(nums[0], gcd(nums[1], nums[-1]))

# 최대공약수의 약수들을 출력함.
for i in range(1, greatest//2 + 1):
    if greatest % i == 0:
        print(i)
print(greatest)