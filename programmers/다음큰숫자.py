def solution(n):
    answer = 0
    one_count = bin(n).count("1")
    while True:
        n += 1
        if bin(n).count("1") == one_count:
            print(n)
            return n
solution(78)