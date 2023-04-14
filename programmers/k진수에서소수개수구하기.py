def solution(n, k):
    answer = 0
    def is_prime(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
            
    
    def change_to_k(n, k):
        num = ''
        while n > 0:
            num += str(n % k)
            n //= k
        return num[::-1]
    
    n_k = change_to_k(n, k)
    n_k_list = n_k.split('0')
    
    for i in range(len(n_k_list)):
        if n_k_list[i] == '1':
            continue
        elif n_k_list[i] == '':
            continue
        tem = int(n_k_list[i])
        if is_prime(tem):
            answer += 1
    return answer