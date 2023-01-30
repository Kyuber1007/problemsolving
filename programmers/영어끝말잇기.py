def solution(n, words):
    # 모든 list 원소들을 한 개씩 순회하면서 검사함
    for i in range(1, len(words)):

        # 현재 말하고 있는 words를 임시로 저장하고
        tem_word = words[i]
        # 1. 끝말 잇기가 아니거나
        # 2. 이미 이전에 말한 단어를 언급하면
        # 탈락하도록 함.
        if tem_word[0] != words[i-1][-1] or (words.count(tem_word) != 1 and words.index(tem_word) != i):
            return [(i % n) + 1, int(i / n) + 1]

    return [0, 0]


solution(3, ["tank", "kick", "know", "wheel",
         "land", "dream", "mother", "robot", "tank"])
