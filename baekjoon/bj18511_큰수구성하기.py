import sys
import itertools


input = sys.stdin.readline

N, K = map(int, input().split())
numbers = set(map(int, input().split()))
N_str = str(N)

max = 0
length = len(N_str)

while length > 0:
    tem = list(itertools.product(numbers, repeat=length))
    for i in tem:
        tem_int = int(''.join(map(str, i)))
        if tem_int <= N and tem_int > max:
            max = tem_int
    if max == 0:
        length -= 1
    else:
        print(max)
        break
