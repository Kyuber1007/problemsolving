import sys
input = sys.stdin.readline
N = int(input().strip())
M = int(input().strip())

room = [[i + 1] for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    index = -1
    for j in range(len(room)):
        if x in room[j]:
            index = j
            break
    tem = index
    new_room = []
    while y not in room[tem]:
        new_room += room[tem]
        tem += 1
    new_room += room[tem]
    room = room[:index] + [new_room] + room[tem + 1:]

print(len(room))