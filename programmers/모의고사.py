def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if supo1[i%5] == answers[i]:
            score[0] += 1
        if supo2[i%8] == answers[i]:
            score[1] += 1
        if supo3[i%10] == answers[i]:
            score[2] += 1
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)
    return answer