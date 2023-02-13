

# arr = input()
# stack = []
# for i in  arr:
#     if not stack:
#         if i in [']', ')']:
#             print(0)
#             exit(0)

#     if i == ')':
#         tem = 0
#         while stack:
#             top = stack.pop()
#             if top =='(':
#                 if tem == 0:
#                     stack.append(2)
#                 else:
#                     stack.append(tem*2)
#                 break
#             elif top == '[':
#                 print(0)
#                 exit(0)
#             else:
#                 tem += int(top)
#     elif i == ']':
#         tem = 0
#         while stack:
#             top = stack.pop()
#             if top =='[':
#                 if tem == 0:
#                     stack.append(3)
#                 else:
#                     stack.append(tem*3)
#                 break
#             elif top == '(':
#                 print(0)
#                 exit(0)
#             else:
#                 tem += int(top)
#     else:
#         stack.append(i)
# try:
#     print(sum(stack))
# except:
#     print(0)