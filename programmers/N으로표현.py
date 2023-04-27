def solution(N, number):
    dp = []
    
    for i in range(1, 9):
        tem_list = set()
        tem_list.add(int(str(N) * i))
        
        for j in range(i//2):
            for tem1 in dp[j]:
                for tem2 in dp[-j-1]:
                    # 더하기
                    tem_list.add(tem1 + tem2)
                    
                    # 뺴기
                    tem_list.add(tem1 - tem2)
                    tem_list.add(tem2 - tem1)
                    
                    # 나누기
                    if tem2 != 0:
                        tem_list.add(tem1 // tem2)
                    if tem1 != 0:
                        tem_list.add(tem2 // tem1)
                    # 곱하기
                    tem_list.add(tem1 * tem2)
        
        if number in tem_list:
            return i
        else:
            dp.append(tem_list)
    return -1