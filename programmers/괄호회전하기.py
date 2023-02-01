# 괄호 확인
def rightness(s):
    arr = []

    # 여는 것만큼 닫는 것도 있는지 확인하기 위한 변수
    check = 0

    # 전체 배열을 돌면서 올바른 괄호인지 확인하기
    for i in range(len(s)):
        # 괄호를 여는 것이 있으면 별도의 배열에 저장
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            arr.append(s[i])
            check += 1
        else:
            if len(arr) <= 0:
                return False
            if s[i] == "]":
                if arr[-1] != "[":
                    return False
            elif s[i] == ")":
                if arr[-1] != "(":
                    return False
            elif s[i] == "}":
                if arr[-1] != "{":
                    return False
            arr.pop()
            check -= 1
    if check != 0:
        return False
    return True


def solution(s):
    answer = 0
    tem_str = s
    for i in range(0, len(s)):
        tem_str = tem_str[1:] + tem_str[0]
        if rightness(tem_str):
            answer += 1
    return answer


# solution("[](){}")
# solution("}]()[{")
solution("((((((")
