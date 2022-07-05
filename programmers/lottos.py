def solution(lottos, win_nums):

    
    count = 0
    zeros = 0
    print(lottos)
    print(win_nums)
    for i in range(len(lottos)):
        num = lottos[i]
        if num == 0:
            zeros += 1
        for j in range(len(win_nums)):
            if num == win_nums[j]:
                count += 1

    answer = [count, count + zeros]
    answer[0] = 7 - (count+zeros) if (7-(count+zeros) < 7) else 6
    answer[1] = 7 - count if(7-count) < 7 else 6
    return answer