from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for i in range(len(discount) - 9):
        if Counter(discount[i:i + 10]) == Counter(want_dict):
            answer += 1
    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
         "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
