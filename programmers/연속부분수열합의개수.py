def solution(elements):
    sum_set = set()
    length = len(elements)
    elements =  elements * 2
    for i in range(length):
        for j in range(length):
            sum_set.add(sum(elements[i:j + i + 1]))

    return len(sum_set)
  
solution([7,9,1,1,4])