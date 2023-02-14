arr = input()
stack = []
flag = 1
count = 0

for i in arr:
    if i == ']':
        tem = 0
        count -= 1
        if stack:
            while stack:
                top = stack.pop()
                if top == '[': 
                    if tem != 0:
                        stack.append(tem * 3)
                        break
                    else: 
                        stack.append(3)
                        break
                elif top == '(':
                    flag = 0
                    break
                else:
                    tem += int(top)
        else:
            flag = 0
            break
    elif i == ')':
        tem = 0
        count -= 1
    
        if stack:
            while stack:
                top = stack.pop()
                if top == '(':
                    if tem != 0:
                        stack.append(tem * 2)
                        break
                    else: 
                        stack.append(2)
                        break
                elif top == '[':
                    flag = 0
                    break
                else:
                    tem += int(top)
        else:
          flag = 0
          break
    else:
        stack.append(i)
        count += 1
    if flag == 0:
        break
      
if flag != 0 and count == 0:
    answer = 0
    while stack:
        answer += int(stack.pop())
    print(answer)
else:
    print(0)