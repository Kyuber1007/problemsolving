n = int(input())

cur_num = 1
stack_list = []
impossible = 0
answer = []

for i in range(n):
    in_num = int(input())
    while in_num >= cur_num:
        stack_list.append(cur_num)
        answer.append("+")
        cur_num += 1
    if in_num == stack_list[-1]: 
        stack_list.pop()
        answer.append("-")
    else:
        impossible = 1
        break 
       
if impossible == 1:
    print("NO")
else:
    for i in range(len(answer)):
        print(answer[i])