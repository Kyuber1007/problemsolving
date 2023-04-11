def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split('.'))
    terms_dict = {}
    
    for i in range(len(terms)):
        a, b = terms[i].split()
        terms_dict[a] = int(b)
        
    for i in range(len(privacies)):
        x, cur_term = privacies[i].split()
        x, y, z = map(int, x.split('.'))
        
        limit = terms_dict[cur_term]
        
        # 유효기간 계산
        year_to_add = (y + limit) // 12
        x += year_to_add
        y = (y + limit) % 12
        z -= 1
        
        # 날짜가 0이거나 달이 0 일 경우 제대로된 숫자 찾아줌
        if z == 0:
            y -= 1
            z = 28
            if y == 0:
                x -= 1
                y = 12
        if y == 0:
            x -= 1
            y = 12
            
        if year > x:
            answer.append(i + 1)
            continue
        elif year == x and month > y:
            answer.append(i + 1)
            continue
        elif year == x and month == y and day > z:
            answer.append(i + 1)
    
    return answer