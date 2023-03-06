import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

candidates = [T]
flag = 0
while candidates:   
    current_ = candidates[0]
    
    if current_ == S:
        flag = 1
        break
    if len(current_) == 0:
        break
    
    if current_[-1] == 'A':
        candidates.append(current_[:-1])
    if current_[0] == 'B':
        new_candidates = ''.join(reversed(current_[1:]))
        candidates.append(new_candidates)
        
    candidates.pop(0)
print(flag)
