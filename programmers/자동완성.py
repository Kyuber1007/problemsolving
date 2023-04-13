def solution(words):
    # 각 단어를 입력해야하는 갯수를 구하기 위한 배열 설정
    answer = [0] * len(words)
    words.sort()
    
    for i in range(len(words) - 1):
        tem1 = words[i]
        tem2 = words[i+1]
        len1 = len(tem1)
        len2 = len(tem2)
        
        # 앞 뒤를 비교해가면서 입력되어야 하는 것들 비교
        for j in range(min(len1, len2)):
            if tem1[j] != tem2[j]:
                # 같은 index까지만 출력하도록 설정
                j -= 1
                break
        # 정답을 구할 때, 같은 갯수보다 1개 더 크게 입력해야하므로 아래와 같이 구함
        answer[i] = max(answer[i], min(len1, j + 2))    
        answer[i+1] = max(answer[i+1], min(len2, j + 2))    
    return sum(answer)