import sys
n = int(sys.stdin.readline())

towers = list(map(int, sys.stdin.readline().split()))
answer = [0 for i in range(n)]
# for i in range(n):
#     cur_height = towers[i]
    
#     if i == 0:
#         answer += "0 "
#     else:
#         tem_index = i - 1
#         candidate_index = i
#         while tem_index >= 0:
#             if towers[tem_index] > cur_height:
#                 candidate_index = tem_index
#                 break
#             tem_index -= 1
#         if candidate_index < 0:
#             answer += "0 "
#         else:
#             answer += f"{candidate_index + 1} "
# print(answer)

stack = []
for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, towers[i]])
    
print(*answer)