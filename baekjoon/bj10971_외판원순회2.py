import sys
input = sys.stdin.readline

N = int(input().strip())
prices = [list(map(int, input().split())) for _ in range(N)]

# 결국 cycle이라서 출발점을 하나로 고정해도 됨
tem = [0]
min_price = -1

def dfs():
    global min_price
    
    if len(tem) == N:
        last_price = prices[tem[-1]][0]
        
        if last_price == 0:
            return
        tem_price = 0
       
        for j in range(1, N):
            tem_price += prices[tem[j-1]][tem[j]]
        tem_price += last_price
        
        if min_price > tem_price or min_price < 0:
            min_price = tem_price
        return
    
    for i in range(1, N):
        tem_set = set(tem)
        if i in tem_set:
            continue
        else:
            if prices[tem[-1]][i] ==0:
                continue
            tem.append(i)
            dfs()
            tem.pop()
    return

dfs()
print(min_price)