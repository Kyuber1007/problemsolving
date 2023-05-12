def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            # 이전 행에서 본인의 index를 제외한 값의 최대를 더해서 현재 행을 업데이트함.
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    
    return max(land[-1])