import sys


input = sys.stdin.readline

N, M = map(int, input().split())
DNAs = []
for i in range(N):
    DNAs.append(input().strip())

count_ = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for j in range(M)]
max_str = ''
hamming_distance = 0
for dna in DNAs:
    for i, text in enumerate(dna):
        count_[i][text] += 1

for i in range(M):
    test = list(max(count_[i].items(), key=lambda x: x[1]))
    max_str += test[0]
    hamming_distance += (N - test[1])
print(max_str)
print(hamming_distance)
