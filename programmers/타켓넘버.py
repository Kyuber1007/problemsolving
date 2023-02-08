def solution(numbers, target):
    test = [0]
    for i in numbers:
        sub = []
        for j in test:
            sub.append(j + i)
            sub.append(j - i)
            test = sub
    return test.count(target)
  
solution([1, 1, 1, 1, 1], 3)