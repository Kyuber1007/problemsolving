def solution(s):
    count = 0
    length = len(s)
    while True:
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count = 1
                s = s[:i-1] + s[i+1:]
            else:
                count = 0

            if len(s) < length:
                length = len(s)
                break
        if count == 0 or len(s) == 0:
            break
    print(1 if len(s) == 0 else 0)
    return 1 if len(s) == 0 else 0


solution("baabaa")
