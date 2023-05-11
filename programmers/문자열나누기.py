def solution(s):
    answer = 0
    
    
    # 초기값 확인
    cur = s[0]
    cur_count = 0
    
    # 앞에서 한글자씩 확인하면서
    for i in range(len(s)):
        # 같으면 증가, 다르면 감소
        if s[i] == cur:
            cur_count += 1
        else:
            cur_count -= 1
            
        # 마지막이라면 1 더하고 (마지막이라면 count가 0이든 아니든 1을 더하면 됨)
        if i+1 == len(s):
            answer += 1
        # 마지막은 아니지만 분기점이 될 때
        elif cur_count == 0:
            answer += 1
            cur = s[i + 1]
            
    return answer