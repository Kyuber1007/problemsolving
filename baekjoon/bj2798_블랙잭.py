import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

tem_max = 0
for i in range(N-2):
    for j in range(i + 1, N-1):
        for k in range(j + 1, N):
            tem = cards[i] + cards[j] + cards[k]
            if tem <= M and tem_max < tem:
                tem_max = tem
print(tem_max)
