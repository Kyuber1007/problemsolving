from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    
    q.append([begin, 0])
    
    while q:
        cur, cur_count = q.popleft()
        if cur == target:
            return cur_count
        
        if cur_count > len(words):
            return 0
        
        for word in words:
            diff = 0
            for j in range(len(cur)):
                if cur[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append([word, cur_count + 1])
        
    return 0