
def solution(operations):
    answer = []
    for i, value in enumerate(operations):
        operands = value.split(" ")
        if operands[0] == "I":
            tem = int(operands[1])
            answer = [tem] + answer
        elif operands[0] == "D" and len(answer) != 0:
            if operands[1] == "1":
                answer.remove(max(answer))
            if operands[1] == "-1":
                answer.remove(min(answer))
    if len(answer) == 0:
        return [0, 0]
    return [max(answer), min(answer)]


# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(["I -45", "I 653", "D 1", "I -642",
         "I 45", "I 97", "D 1", "D -1", "I 333"])
