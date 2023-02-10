# Counter를 이용해서 최대값을 동시에 처리하는 풀이 
def solution(n, works):
    answer = 0
    from collections import Counter
    answer_counter = Counter(works)
    test = sorted(list(answer_counter.items()))
    time_list = [list(tup) for tup in test]
    
    if sum(works) < n:
        return 0
    
    while n > 0:
        key, value = time_list.pop()

        if n >= value:
            if time_list and time_list[-1][0] == key - 1:
                time_list[-1][1] += value
                n -= value
            else:
                time_list.append([key - 1, value])
                n -= value
        else:
            time_list.append([key - 1, n])
            time_list.append([key, value - n])
            n = 0
    for i in range(len(time_list)):
        tem = 0
        key = time_list[i][0]
        value = time_list[i][1]
        while tem < value:
            tem += 1
            answer += key**2
    return answer

# heapq를 이용한 풀이 
def solution(n, works):
    if sum(works) < n:
        return 0
    from heapq import heapify, heappop, heappush
    heapify(works_heap := [-i for i in works])
    while n > 0:
        heappush(works_heap, heappop(works_heap) + 1)
        n -= 1
    return sum([i**2 for i in works_heap])


# def solution(n, works):
    # print(all(works) > 2)
    # answer = 0
    # if sum(works) <= n:
        # return 0
      # 
    # for i in range(n):
        # works.sort()
        # works[-1] -= 1
        # n -= 1
    # 
    # for i in range(len(works)):
        # answer += works[i]**2
    # return answer
  

solution(4, [3, 4, 3])