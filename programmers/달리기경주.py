def solution(players, callings):
    answer = []
    player_name_dict = {}
    rank_dict = {}
    
    for idx, name in enumerate(players):
        player_name_dict[name] = idx + 1
        rank_dict[idx + 1] = name
    for name in callings:
        # 현재 호명된 사람의 순위
        rank = player_name_dict[name]
        # 이전 플레이어의 이름
        prev_player = rank_dict[rank - 1]
        player_name_dict[prev_player] += 1
        player_name_dict[name] -= 1
        
        rank_dict[rank - 1] = name
        rank_dict[rank] = prev_player
        
    return list(rank_dict.values())
