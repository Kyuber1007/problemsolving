def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    print(name_dict)
    
    for pp in photo:
        tem = 0
        for person in pp:
            if name_dict.get(person):
                tem += name_dict[person]
            
        answer.append(tem)
    return answer