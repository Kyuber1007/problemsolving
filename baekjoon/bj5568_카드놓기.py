import sys
import itertools
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
numbers = []

for i in range(n):
    numbers.append(input().strip())

result = set()

for num in itertools.permutations(numbers, k):
    result.add(int(''.join(num)))
print(len(result))
