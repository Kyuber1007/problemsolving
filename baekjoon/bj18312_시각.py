import sys
input = sys.stdin.readline

N, K = map(int, input().split())

count = 0
for i in range(N + 1):
    tem_str = str(i).zfill(2)
    if str(K) in tem_str:
        count += 3600
        continue
    for j in range(60):
        tem_str = str(j).zfill(2)
        if str(K) in tem_str:
            count += 60
            continue
        for k in range(60):
            tem_str = str(k).zfill(2)
            if str(K) in tem_str:
                count += 1
print(count)
