a = input()

for i in range(int(a)):
    b = map(str, input().split())
    b = list(b)
    num = float(b[0])
    for j in range(1, len(b)):
        if b[j] == '@':
            num = num *3
        elif b[j] == '%':
            num = num + 5
        elif b[j] == '#':
            num = num - 7
    
    print("{:.2f}".format(num))
    