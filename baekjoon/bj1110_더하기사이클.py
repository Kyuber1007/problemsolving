n = int(input())

count = 0
re_ = -1

while n != re_:
    if count == 0:
        re_ = n
    if re_ < 10:
        add_result = int(re_)
    else:
        add_result = re_ % 10 + re_ // 10
    re_ = (re_ % 10) * 10 + add_result % 10
    count += 1
print(count)
