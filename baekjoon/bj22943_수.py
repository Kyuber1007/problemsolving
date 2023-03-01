import sys 
import math
K, M = map(int, sys.stdin.readline().split())

num = 2
flag = 1
prime_list = []
candidiates = []

while num < 10 ** K:
    for i in range(2, int(math.sqrt(num)) + 1): 
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        prime_list.append(num)
    else:
        flag = 1
    num += 1

def check_possibility(tem_list):
    test = {}
    for i in range(10):
        test[str(i)] = False
    for i in range(len(tem_list)):
        if test[tem_list[i]] == True:
            return False
        else:
            test[tem_list[i]] = True
    return True
print(prime_list)
# for i in range(len(prime_list) - 1):
#     for j in range(i + 1, len(prime_list)):
#         tem = prime_list[i] + prime_list[j]
#         if tem < 10 ** K and tem  >= 10 ** (K - 1): 
#             tem_list = str(tem)
#             if tem not in candidiates and check_possibility(tem_list):
#                 candidiates.append(tem)
print(candidiates.sort())
            