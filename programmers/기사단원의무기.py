def solution(number, limit, power):
    answer = 0
    
    def get_divisor_count(number):
        count = 0
        for i in range(1, int(number ** (1/2)) + 1):
            if number % i == 0:
                if i * i == number:
                    count += 1
                else:
                    count += 2
        return count
            
    for i in range(1, number + 1):
        # 약수 갯수 구하는 함수
        count = get_divisor_count(i)
        
        if count > limit:
            answer += power
            
        else:
            answer += count
    return answer