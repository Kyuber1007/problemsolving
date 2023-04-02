import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    nums = list(map(int, input().split()))
    min_, max_ = nums[0], nums[0]
    
    for j in nums:
        if min_ > j:
            min_ = j
        if max_ < j: 
            max_ = j
    print(min_, max_)