import sys
input = sys.stdin.readline

N = int(input().strip())
num_list = list(map(int, str(N)))
num_sum = sum(num_list)
length = len(num_list)

tem = N - 9 * length
if tem < 0:
    tem = 0
min_ = 0
while tem < N:
    tem += 1

    tem_list = list(map(int, str(tem)))
    if tem + sum(tem_list) == N:
        min_ = tem
        print(min_)
        break

if min_ == 0:
    print(0)
