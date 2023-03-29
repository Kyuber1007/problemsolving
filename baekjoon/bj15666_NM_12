import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

tem =  []
result = set()

cur_i = 0

def dfs():
    global cur_i
    
    if len(tem) == M:
        new_str = ' '.join(str(nums[i]) for i in tem)
        if new_str in result:
            return
        else:
            result.add(new_str)
            print(new_str)
            return
    for i in range(N):
        if cur_i <= i:
            tem.append(i)
            cur_i = tem[-1]
            dfs()
            tem.pop()
            if len(tem) > 0:
                cur_i = tem[-1]
    return
  
dfs()