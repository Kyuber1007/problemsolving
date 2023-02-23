import sys
input = sys.stdin.readline
n, m = map(int, input().split())

n_set = set()
for i in range(n):
    n_set.add(input())
    
count = 0
for i in range(m):
    test_str = input()
    if test_str in n_set:
        count += 1
        
print(count)