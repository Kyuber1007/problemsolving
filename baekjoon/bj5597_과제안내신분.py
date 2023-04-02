import sys
input = sys.stdin.readline

done = [0] * 30

for i in range(28):
    done[int(input().strip()) -1] = 1
for i in range(30):
    if done[i] == 0:
        print(i + 1)