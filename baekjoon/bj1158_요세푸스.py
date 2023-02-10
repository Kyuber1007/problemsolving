N, K = map(int, input().split())

people = [i for i in range(1, N + 1)]
result = []
index = K - 1
s = "<"

result.append(people[index])
tem = people.pop(index)
s += str(tem) + ", "

while len(result) < N:
    index += (K - 1)

    while index >= len(people):
        index -= len(people)

    result.append(people[index])
    s += str(people.pop(index)) + ", "

s = s[:-2] + ">"
print(s)
