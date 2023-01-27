def solution(s):
    count = 0
    removed_zeros = 0
    

    while s != "1":
        removed_zeros += s.count("0")
        s = "1" * (len(s) - s.count("0"))
        s = str(bin(len(s)))[2:]
        print(s)
        count += 1
    return [count,removed_zeros]
  
solution("110010101001")