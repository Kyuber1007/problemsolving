def solution(numbers):
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i])
    
    def is_prime(test):
        if test == 1 or test == 0:
            return False
        for i in range(2, int(test ** 0.5) + 1):
            if test % i == 0:
                return False
        return True            

    visited = [0] * len(nums)
    tem = []
    result = set()
    def dfs():
        if len(tem) > 0:
            test_num = int(str(''.join(tem)))
            if is_prime(test_num):
                result.add(test_num)
        for i in range(len(nums)):
            if visited[i] == 0:
                visited[i] = 1
                tem.append(nums[i])
                dfs()
                visited[i] = 0
                tem.pop()
    dfs()
    return len(result)