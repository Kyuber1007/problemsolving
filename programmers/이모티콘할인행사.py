
def dfs(idx, users, emoticons):
    global answer1, answer2
    
    if idx == len(emoticons):
        emoticon_plus = [0] * len(users)
        users_usage = [0] * len(users)
        
        for j in range(len(emoticons)):
            for k in range(len(users)):
                
                # 할인율이 본인 기준보다 크고, 이모티콘 가입자가 아닐 때 이모티콘을 구매함
                if emoticon_plus[k] == 0 and users[k][0] <= discount[j]:
                    tem = users_usage[j] + emoticons[j]
                    if tem >= users[k][1]:
                        users_usage[j] = 0
                        emoticon_plus[j] = 1
        if answer1 <= sum(emoticon_plus) and sum(users_usage) > answer2:
            answer1 = sum(emoticon_plus)
            answer2 = sum(users_usage)
        return
      
    for i in range(4):
        discount.append(discount_range[i])
                        
        
def solution(users, emoticons):
    dfs(0, users, emoticons)

discount_range = [10, 20, 30, 40]
    
answer1 = 0
answer2 = 0    
discount = []
    
solution([[40, 10000], [25, 10000]], [7000, 9000])