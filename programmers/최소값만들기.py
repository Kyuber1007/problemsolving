def solution(s):
    answer = ''
   
    for i, c in enumerate(s):
        if i == 0:
            answer += c.upper()
        else:
            if s[i-1] == " ":
                answer += c.upper()
            else:
                answer += c.lower()
    return answer