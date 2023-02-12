input_str = input()

answer = 0
cur_stick = 0

# 전체 string을 돌면서 파악
for i in range(len(input_str) -1):
    # ( 가 들어왔을 때, laser인지 아닌지 구분하는 것이 필요함.
    if input_str[i] == "(":
        # laser라면 현재 stick이 쪼개지는 것이므로 현재 stick의 갯수만큼 추가함.
        if input_str[i+1] == ")":
            answer += cur_stick
        # 새로운 stick 이라면 cur_stick을 추가하고, answer를 한 개 늘림
        # 정답 stick을 한 개 추가하고, 쪼개질 수 있는 후보군에 등록해 놓는 것. 
        else:
            cur_stick += 1
            answer += 1
    # stick이 끝나는 단계라면, cur_stick을 감소시킴.
    # 어차피 string의 시작이 )일 경우는 없기 떄문에 index error는 발생하지 않음
    if input_str[i] == ")":
        if input_str[i - 1] != "(":
            cur_stick -= 1
print(answer)