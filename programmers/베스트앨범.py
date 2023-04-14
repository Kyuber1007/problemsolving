def solution(genres, plays):
    answer = []
    musics = []
    
    # 재생횟수 세기
    count = {}
    for music in zip(genres, plays):
        if count.get(music[0]):
            count[music[0]] += music[1]
        else:
            count[music[0]] = music[1]
    count_items = list(count.items())
    count_items.sort(key=lambda x:(x[1]), reverse=True)
    
    # 음악을 같은 장르끼리 모이게, 그리고 재생횟수 순서대로 모으기
    for i in range(len(genres)):
        musics.append([i, genres[i], plays[i]])
    musics.sort(key=lambda x: (x[1], x[2]), reverse=True)
    
    for i in range(len(count_items)):
        cur_genre = count_items[i]
        idx = 0
        
        while idx < len(musics) and musics[idx][1] != cur_genre[0]:
            idx += 1
            if idx == len(musics):
                break
        
        tem = idx
        while idx < len(musics) and idx - tem < 2 and musics[idx][1] == cur_genre[0]:
            answer.append(musics[idx][0])
            idx += 1
    return answer