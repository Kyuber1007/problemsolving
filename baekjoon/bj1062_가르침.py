# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())

# words = []
# learned = [0] * 26

# for i in range(N):
#     words.append(input().strip())
    
# if K < 5:
#     print(0)
#     exit()
# elif K == 26:
#     print(N)
#     exit()
    
# for c in ['a', 'c', 't','i', 'n']:
#     learned[ord(c) - ord('a')] = 1
    
# answer = 0

# def dfs(idx, learned_num):
#     global answer
    
#     if learned_num == K:
#         tem = 0
        
#         for w in words:
#             flag = True
#             for c in w:
#                 if not learned[ord(c) - ord('a')]:
#                     flag = False
#                     break
#             if flag:
#                 tem += 1
#             answer = max(answer, tem)
#         return
      
#     for i in range(idx, 26):
#         if not learned[i]:
#             learned[i] = 1
#             dfs(i, learned_num + 1)
#             learned[i] = 0
  
# dfs(0, 5)
# print(answer)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = []

for i in range(N):
    words.append(input().strip())

learned = [0] * 26

for c in ['a', 't', 'n', 'c', 'i']:
    learned[ord(c) - ord('a')] = 1
    
answer = 0
def dfs(idx, learned_num):
    global answer
    
    if learned_num == K:
        tem = 0
        for w in words: 
            flag = True
            for c in w:
                if learned[ord(c) - ord('a')] == 0:
                    flag = False
                    break
            if flag:
                tem += 1
        answer = max(answer, tem)
        return
    for i in range(idx, 26):
        if learned[i] == 0:
            learned[i] = 1
            dfs(i, learned_num + 1)
            learned[i] = 0

if K < 5:
    print(0)
elif K == 26:
    print(N)

else:
    dfs(0, 5)
    print(answer)