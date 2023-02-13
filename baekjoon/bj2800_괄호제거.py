# input에서 모든 괄호의 대응쌍들을 지울 수 있는 경우를 출력하는 문제
input_str = input()

bracket_open = []
bracket_set = []
# 중복을 제거하기 위해 집합으로 만듦
answer = set()

# input string을 돌면서, 괄호 대응쌍을 전부 찾음
for i, value in enumerate(input_str):
    if value == '(':
        bracket_open.append(i)
    elif value == ')':
        tem = bracket_open.pop()
        bracket_set.append([tem, i])

from itertools import combinations
# 전부 찾은 대응쌍들을 combination을 통해 없앨 것들을 고름
# 1개부터 시작해서, 전체 갯수만큼. 0개를 없애는 경우는 존재하지 않음
for i in range(1, len(bracket_set) + 1):
    for candidates in combinations(bracket_set, i):
        # input을 list로 바꿔서 해당하는 index를 ''빈칸으로 바꿈
        tem_input = list(input_str)
        for j in candidates:
            tem_input[j[0]] = ""
            tem_input[j[1]] = ""
        # string으로 만들어서 추가함.
        answer.add(''.join(tem_input))
answer = list(answer)
answer.sort()
for i in answer:
    print(i)