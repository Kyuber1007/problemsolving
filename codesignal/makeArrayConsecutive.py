def solution(statues):
    max_num = max(statues)
    min_num = min(statues)
    
    return (max_num - min_num) - len(statues) + 1
