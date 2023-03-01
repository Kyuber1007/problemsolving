import sys

input = sys.stdin.readline

N = int(input())

people = list(map(int, input().split()))

people.sort()
per_people = []
tem = 0
for i, value in enumerate(people):
    if i > 0:
        tem = per_people[i - 1] + value
        per_people.append(tem)
    else:
        per_people.append(value)
print(sum(per_people))
