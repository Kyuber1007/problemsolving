
def solution(numbers):
    answer = ''
    n = len(numbers)
    num_ = []
    
    for i in range(n):
        num_.append(str(numbers[i]))
    num_.sort(reverse=True, key=lambda num:num*3)
    
    return str(int(''.join(num_)))