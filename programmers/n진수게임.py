from collections import deque

def solution(n, t, m, p):
    answer = ''
    
    queue = deque()
    
    # 뽑아야되는 순서 기록
    for i in range(t):
        queue.append(p-1 + m * i)
    idx = 0
    cur_num = 0
    
    # 진법 변환
    def cur_num_to_n(cur_num):
        changed_list = deque()

        while cur_num // n > 0:
            changed_list.append(str(cur_num % n))
            cur_num //= n
        changed_list.append(str(cur_num))
        changed_list.reverse()
        
        if n > 10:
            for i in range(len(changed_list)):
                cur_idx_num = int(changed_list[i])
                if cur_idx_num >= 10:
                    if cur_idx_num == 10:
                        changed_list[i] = 'A'
                    elif cur_idx_num == 11:
                        changed_list[i] = 'B'
                    elif cur_idx_num == 12:
                        changed_list[i] = 'C'
                    elif cur_idx_num == 13:
                        changed_list[i] = 'D'
                    elif cur_idx_num == 14:
                        changed_list[i] = 'E'
                    elif cur_idx_num == 15:
                        changed_list[i] = 'F'
        return changed_list
    
    num = 0
    idx = 0    
    total_num_list = []
    
    # 내가 말해야하는 순서동안에
    while queue:
        cur_idx = queue.popleft()
        # idx보다 더 크게 total_num_list
        while cur_idx >= len(total_num_list):
            num_list = cur_num_to_n(num)
            total_num_list += num_list
            num += 1
        answer += total_num_list[cur_idx]
    return answer