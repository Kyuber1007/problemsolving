def solution(d, budget):
    answer = 0
    a = len(d)
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if(budget < 0):
            print(i)
            return i
        
d = [1, 3, 2, 5, 4]
solution(d, budget=9)