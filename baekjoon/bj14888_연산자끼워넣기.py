# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# nums = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
# min_, max_ = True, True
# count = 0
# def dfs(idx, result):
#     global add, sub, mul, div, min_, max_, count
#     if idx == N:
#         if count == 0:
#             min_ = result
#             max_ = result
#             count += 1
#         else:
#             min_ = min(min_, result)
#             max_ = max(max_, result)
#         return
#     if add > 0:
#         add -= 1
#         dfs(idx + 1, result + nums[idx])
#         add += 1
        
#     if sub > 0:
#         sub -= 1
#         dfs(idx + 1, result - nums[idx])
#         sub += 1
        
#     if mul > 0:
#         mul -= 1
#         dfs(idx + 1, result * nums[idx])
#         mul += 1
        
#     if div > 0:
#         div -= 1
#         dfs(idx + 1, int(result / nums[idx]))
#         div += 1
        
# dfs(1, nums[0])

# print(max_)
# print(min_)


import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_, min_ = True, True
count = 0
def dfs(idx, result):
    global count, max_, min_, add, sub, mul, div
    
    if idx == N:
        if count == 0:
            min_ = result
            max_ = result
            count += 1
        else:
            if min_ > result:
                min_ = result
            if max_ < result:
                max_ = result
            # min_ = min(result, min_)
            # max_ = max(result, max_)
        return
    
    if add > 0:
        add -= 1
        dfs(idx + 1, result + nums[idx])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(idx + 1, result - nums[idx])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(idx + 1, result * nums[idx])
        mul += 1
    if div > 0:
        div -= 1
        dfs(idx + 1, int(result / nums[idx]))
        div += 1
    return


dfs(1, nums[0])
print(max_)
print(min_)