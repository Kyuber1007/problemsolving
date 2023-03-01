import sys
import math

N = int(sys.stdin.readline())

def test_prime(N):
    if N == 0 or N == 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True
  
def test_pelindrome(N):
    N_list = str(N)
    length = len(N_list)
    
    for i in range(int(length/2) + 1):
        if N_list[i] != N_list[length - (i + 1)]:
            return False
    return True

while True:
    if test_prime(N) and test_pelindrome(N):
        print(N)
        break
    N += 1