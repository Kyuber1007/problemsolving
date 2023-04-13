def solution(m, musicinfos):
    answer = [0, '']
    
    # 기억하고 있는 멜로디를 리스트로 변환
    new_m = []
    for i in range(len(m)):
        if not m[i].isalpha():
            new_m[-1] += m[i]
        else:
            new_m.append(m[i])
        
    # 각 음악 정보들을 확인
    for i in range(len(musicinfos)):
        cur_music = musicinfos[i].split(',')

        time1 = int(cur_music[0][:2]) * 60 + int(cur_music[0][3:5])
        time2 = int(cur_music[1][:2]) * 60 + int(cur_music[1][3:5])
        time_duration = time2 - time1
        
        tem_melody = []
        
        # 음악 멜로디를 리스트로 전환.
        for j in range(len(cur_music[3])):
            if not cur_music[3][j].isalpha():
                tem_melody[-1] += cur_music[3][j]
            else:
                tem_melody.append(cur_music[3][j])
        
        # 음악을 재생시간만큼 반복
        if time_duration < len(tem_melody):
            tem_melody = tem_melody[:time_duration + 1]
        else:
            l = 0
            while len(tem_melody) < time_duration:
                tem_melody.append(tem_melody[l])
                l += 1
        
        # 일치 하는지 확인하기
        l = 0
        melody_idx = 0
        
        flag = False
        while melody_idx < len(tem_melody):
            if new_m[0] == tem_melody[melody_idx]:
                tem = melody_idx
                while tem < len(tem_melody):
                    # 같은지 아닌지를 점차 비교하기
                    if tem_melody[tem] == new_m[l]:
                        l += 1
                        tem += 1
                    else: 
                        l = 0
                        break
                    # 비교 종료 조건 == l 이 new_m의 길이가 되면 전부 다 같음을 의미함.
                    if l == len(new_m):
                        flag = True
                        break
            if flag:
                answer_candidate_duration = time_duration
                answer_candidate_name = cur_music[2]
                if answer_candidate_duration > answer[0]:
                    answer[0] = answer_candidate_duration
                    answer[1] = answer_candidate_name
                break
            melody_idx += 1
    if answer[0] == 0:
        return '(None)'
    else:
        return answer[1]
      