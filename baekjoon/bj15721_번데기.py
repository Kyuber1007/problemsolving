import sys
input = sys.stdin.readline

A = int(input())
T = int(input())
which = int(input())

count = 0
time = 0

while count + (4 + time) < T:
    count += 4 + time
    time += 1
people_count = count * 2

if T - count <= 2:
    count += 1
    if count == T:
        if which == 0:
            people_count += 1
        else:
            people_count += 2
    else:
        if which == 0:
            people_count += 3
        else:
            people_count += 4
else:
    count += 2
    people_count += 4
    if which != 0:
        people_count += (time + 2)
    for i in range(time + 2):
        count += 1
        people_count += 1
        if count == T:
            break
print((people_count-1) % A)
