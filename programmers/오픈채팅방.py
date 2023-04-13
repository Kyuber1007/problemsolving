def solution(record):
    answer = []
    id_name_dict = {}

    # 최종 이름을 저장하기 위한 dictionary    
    for i in range(len(record)):
        line = record[i].split(' ')
        if not line[0] == 'Leave':
            id_name_dict[line[1]] = line[2]
            
    # 결과를 나타내기 위한 부분
    for i in range(len(record)):
        line = record[i].split(' ' )
        if line[0] == 'Enter':
            answer.append(f'{id_name_dict[line[1]]}님이 들어왔습니다.')
        elif line[0] == 'Leave':
            answer.append(f'{id_name_dict[line[1]]}님이 나갔습니다.')
    return answer