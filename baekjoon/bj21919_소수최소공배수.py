import sys
import math
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

# 소수 여부를 따져야함. 0, 1 주의
def test_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

result = 1
prime_list = []
# 소수의 최소공배수는 그냥 곱임.
# 단, 같은 값 여부를 확인해야함.
for i in range(N):
    if test_prime(A[i]) and result != A[i]:
        result *= A[i]

if result == 1:
    print(-1)
else:
    print(result)