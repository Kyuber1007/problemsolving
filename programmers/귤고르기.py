def solution(k, tangerine):
    answer = 0
    
    # 크기 별로 묶기 쉽게 정렬해줌
    tangerine.sort()

    count = []
    index = 0
    
    # 크기별로 갯수를 세고, list에 값 update.
    for i, val in enumerate(tangerine):
        if i == 0:
            count.append(1)
        else:
            if val == tangerine[i - 1]:
                count[index] += 1
            else: 
                index += 1
                count.append(1)
    # 같은 크기가 많은 것부터 정렬해줌
    count = sorted(count, reverse=True)
  
    for i in range(len(count)):
        k = k - count[i]
        answer += 1
        if k <= 0:
            return answer
  
solution(6, [1, 3, 2, 5, 4, 5, 2, 3])