cnt = int(input())
a = [0 for i in range(cnt)]

for i in range(len(a)):
    new_in = int(input())
    a[i] = new_in
    for j in range(i + 1):
        if a[j+1] > new_in:
            tem = a[j]
            a[j] = new_in
            new_in = tem
        
    print(a)
print(a)  