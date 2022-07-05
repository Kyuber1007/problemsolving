cnt = int(input())

for i in range(cnt):
    a, b = map(int, input().split())
    m = a * b
    gcd = a
    while(b > 0):
        tem = gcd
        gcd = b
        b = tem % b

    print(int(m/gcd))