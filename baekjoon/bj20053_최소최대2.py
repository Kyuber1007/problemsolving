import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    nums = list(map(int, input().split()))
    min_, max_ = True,True
    for j in range(len(nums)):
        if min_ == True and max_ == True:
            min_, max_ = nums[j], nums[j]
        else:
            if min_ > nums[j]:
                min_ = nums[j]
            if max_ < nums[j]: 
                max_ = nums[j]
    print(min_, max_)