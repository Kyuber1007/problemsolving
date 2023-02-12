# bracket_str = input()

# bracket_stack = []
# tem = 0
# flag = 1

# for i in bracket_str:
#     if not bracket_stack:
#         if i in [']', ')']:
#             flag = 0
#             break
          
#     if i == ')':
#         tem = 0
#         while bracket_stack:
#             top = bracket_stack.pop()
#             if top == '(':
#                 if tem == 0:
#                     bracket_stack.append(2)
#                 else:
#                     bracket_stack.append(tem * 2)
#                 break
#             elif top == '[':
#                 flag = 0
#                 break
#             else:
#                 tem += int(top)
                
#     elif i == ']':
#         tem = 0
#         while bracket_stack:
#             top = bracket_stack.pop()
#             if top == '[':
#                 if tem == 0:
#                     bracket_stack.append(3)
#                 else:
#                     bracket_stack.append(tem * 3)
#                 break
#             elif top == '(':
#                 flag = 0
#                 break
#             else:
#                 tem += int(top)
#     else:
#         bracket_stack.append(i)

# if flag == 1:
#     print(sum(bracket_stack))
# else:
#     print(0)


arr = input()
stack = []
for i in  arr:
    if not stack:
        if i in [']', ')']:
            print(0)
            exit(0)

    if i == ')':
        tem = 0
        while stack:
            top = stack.pop()
            if top =='(':
                if tem == 0:
                    stack.append(2)
                else:
                    stack.append(tem*2)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                tem += int(top)
    elif i == ']':
        tem = 0
        while stack:
            top = stack.pop()
            if top =='[':
                if tem == 0:
                    stack.append(3)
                else:
                    stack.append(tem*3)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                tem += int(top)
    else:
        stack.append(i)
try:
    print(sum(stack))
except:
    print(0)