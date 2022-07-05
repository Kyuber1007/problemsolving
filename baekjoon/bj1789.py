num = input()
i = 1
sum = 0
while sum < int(num):
    sum = sum + i
    i = i + 1
if sum == int(num):
    print(i - 1)
else:
    print(i-2)    