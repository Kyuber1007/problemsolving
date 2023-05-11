def solution(s):
    answer = []
    
    # 사용한 알파벳의 현황을 알려주기 위한 dictionary
    alphabets = {}
    
    # 한글자씩 순회하면서
    for i in range(len(s)):
        if s[i] not in alphabets:
            answer.append(-1)
        else:
            answer.append(i - alphabets[s[i]])
        # 마지막 위치로 값을 수정함
        alphabets[s[i]] = i
    return answer