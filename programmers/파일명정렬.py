def solution(files):
    answer = []
    files_ = []
    
    for i in range(len(files)):
        cur_name = files[i]
        cur_length = len(cur_name)
        
        num_start = cur_length
        num_end = 0
        
        flag = True
        idx = 0
        # 현재 파일의 파트를 나누는 부분
        # Number 부분의 시작과 끝을 나눔    
        while idx < cur_length and flag:
            if cur_name[idx].isdigit() and flag:
                flag = False
                num_start = idx
                while  idx < cur_length and cur_name[idx].isdigit():
                    num_end = idx
                    idx += 1
            idx += 1
            
        # Tail 존재 여부에 따라 다르게 표현
        tail = ''
        if num_end < cur_length - 1:
            tail = cur_name[num_end + 1:]
        files_.append([i, cur_name[:num_start].lower(), int(cur_name[num_start:num_end + 1]), tail])
        files_.sort(key=lambda x: (x[1], x[2]))
        
    for i in range(len(files_)):
        answer.append(files[files_[i][0]])
    
    return answer