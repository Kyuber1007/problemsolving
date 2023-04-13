def solution(msg):
    answer = []
    dictionary = {}
    dict_len = 26
    dict_max_len = 1
    
    for i in range(26):
        dictionary[chr(ord('A') + i)] = i + 1
    
    while msg:
        cur_in = msg[:dict_max_len]
        # 현재 입력과 일치하는 가장 긴 dict mem을 찾는 과정
        tem = dict_max_len
        
        while len(cur_in) > 1:
            test_ = msg[:tem]
            if test_ not in dictionary:
                tem -= 1
                cur_in = msg[:tem]
            else: break

        # 색인을 출력 및 메세지 제거
        answer.append(dictionary[cur_in])
        
        msg = msg[len(cur_in):]
        
        # 다음 것을 색인에 등록
        if msg:
            dict_len += 1
            new_dict_in = cur_in + msg[0]
            dictionary[new_dict_in] = dict_len
            dict_max_len = max(len(new_dict_in), dict_max_len)
    return answer
  
solution("KAKAO")