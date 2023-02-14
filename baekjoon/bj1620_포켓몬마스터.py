import sys
input = sys.stdin.readline

pocketmons_hash = {}
pocketmons_hash2 ={}
n, m = map(int, input().split())

for i in range(n):
    pocketmon = input().strip()
    pocketmons_hash[i] = pocketmon
    pocketmons_hash2[pocketmon] = i

for i in range(m):
    question = input().strip()
    if question.isalpha():
        print(pocketmons_hash2.get(question) + 1)
    else:
        print(pocketmons_hash.get(int(question) -1))