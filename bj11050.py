a, b = map(int, input().split())
c = a - b
cnt = 1
for i in range(a):
    if b < c:
        tem = b
        b = c
        c = tem
    if (i+1) > b:
        cnt = (i + 1) * cnt 
    
for j in range(c):
    cnt /= (j+1)

print(int(cnt))