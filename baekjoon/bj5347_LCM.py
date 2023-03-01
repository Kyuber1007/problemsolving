import sys

input = sys.stdin.readline

n = int(input())

def LCM(a, b):
    return a * b/ GCD(a, b)
  
def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return (GCD(b, a%b))
    
    
for i in range(n):
    a, b = map(int, input().split())
    print(int(LCM(a, b)))