import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

tem = []
result = set()

def dfs():
    if len(tem) == M:
        new_str = ' '.join(str(nums[i]) for i in tem)
        if new_str in result: 
            return
        result.add(new_str)
        print(new_str)
        return
      
      
    for i in range(N):
        tem.append(i)
        dfs()
        tem.pop()
    return


dfs()