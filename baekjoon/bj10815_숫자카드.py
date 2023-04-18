import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

M = int(input())
M_nums = list(map(int, input().split()))

nums.sort()

def binary_search(num, start, end):

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == num:
            return True
        elif nums[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return False
  
for i in M_nums:
    result = binary_search(i, 0, N - 1)
    if result:
        print('1', end=' ')
    else:
        print('0', end=' ')