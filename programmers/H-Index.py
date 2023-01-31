# 도무지 설명을 이해할 수 없음.
def solution(citations):

    citations.sort()
    length = len(citations)
    index = length - 1

    while True:
        tem = citations[index]
        if tem > length - index:
            index -= 1
        else:
            print(tem)
            return tem


solution([3, 0, 6, 1, 7, 5, 5, 5, 5, 5, 7])
