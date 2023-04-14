def solution(nums):
    answer = 0
    
    nums.sort()
    N = len(nums)

    result = {}
    for i in range(N):
        if result.get(nums[i]):
            result[nums[i]] += 1
        else:
            result[nums[i]] = 1
    if len(result) >= N//2:
        return N//2
    else:
        return len(result)
    
    return answer