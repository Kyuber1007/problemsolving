from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
problem_string = input()

cnt = {'B': 0, 'R': 0}
cnt[problem_string[0]] += 1

for i in range(1, N):
    if problem_string[i] != problem_string[i - 1]:
        cnt[problem_string[i]] += 1
print(min(cnt['B'], cnt['R']) + 1)
