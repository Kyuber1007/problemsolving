import sys
n = int(sys.stdin.readline())

for i in range(n):
    string = sys.stdin.readline()
    count = 0
    open_count = 0
    result = True
    while count < len(string) - 1:
        if string[count] == '(':
            open_count += 1
        elif string[count] == ')':
            open_count -= 1

        if open_count < 0:
            result = False
            break
        count += 1

    if open_count == 0 and result == True:
        print("YES")
    else:
        print("NO")
