import sys
input = sys.stdin.readline

N = int(input())

total_people = 0

places = []
for i in range(N):
    new_place, new_people = map(int, input().split())
    total_people += new_people
    places.append([new_place, new_people])

places.sort()

count = 0
for i in range(N):
    count += places[i][1]
    if count >= total_people/2:
        print(places[i][0])
        break
