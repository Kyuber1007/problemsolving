def solution(clothes):
    answer = 1
    clothes_dict = {}

    for i in range(len(clothes)):
        if clothes[i][1] in clothes_dict:
            clothes_dict[clothes[i][1]] += 1
        else:
            clothes_dict[clothes[i][1]] = 1
    for value in clothes_dict.values():
        answer *= (value + 1)
    return answer - 1


solution([["yellow_hat", "headgear"], ["blue_sunglasses",
         "eyewear"], ["green_turban", "headgear"]])
