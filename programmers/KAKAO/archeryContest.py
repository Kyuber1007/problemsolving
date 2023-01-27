def solution(n, info):
    answer = [0]*11 # 정답을 넘기기 위한 배열
    arr = [0]*11 # 라이언의 경우의 수를 계산하기 위한 배열
    max_diff = 0
    
    # 점수판에서 발생할 수 있는 모든 경우의 수 고려
    for subset in range(1, 1<<10):
        ryan = 0
        peach = 0
        cnt = 0 # 라이언이 맞춘 화살의 갯수
        
        # 각 점수 별로 승자를 비교
        for i in range(10):
            # subset은 라이언이 1 ~ 10 중에서 이긴 점수의 수를 표현하기 위한 bit
           
            # 만약에 ryan이 이긴 점수판이라면,
            # 해당 점수를 ryan에게 추가하고, 맞춘 화살의 갯수를 표시함. 
            if subset & (1<<i):
                ryan += 10 - i
                arr[i] = info[i] + 1
                cnt += arr[i]
            # ryan이 진 점수판이라면, 
            # 한 개도 못맞춘 것으로 해서 화살을 아끼도록 함.
            else:
                arr[i] = 0
                if info[i]:
                    peach += 10 - i

        # 화살의 갯수가 조건보다 초과하면 따지지 않도록 함. 
        if cnt > n: continue

        # 버리는 화살들은 0점에 맞춘 것으로 함.
        arr[10] = n - cnt

        # max를 따지는 방식
        # 1. max_diff와 같은 값을 가질 때 -> 낮은 점수를 더 많이 맞춘 경우를 max로
        if ryan - peach == max_diff:
            for j in reversed(range(11)):
                if arr[j] > answer[j]:
                    answer = arr[:]
                    break
                elif arr[j] < answer[j]:
                    break
                
        # 2. 새로운 max 값을 가질 때
        if ryan - peach > max_diff:
            max_diff = ryan - peach
            answer = arr[:]
        
    if max_diff == 0:
        return [-1]   
    return answer


n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
solution(n, info)