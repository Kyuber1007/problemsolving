def solution(inputString):
    print(set(inputString))
    return sum([inputString.count(i) % 2 for i in set(inputString)]) < 2