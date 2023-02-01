def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tem_row = []
        for j in range(len(arr2[0])):
            tem = 0
            for k in range(len(arr2)):
                tem += (arr1[i][k] * arr2[k][j])
            tem_row.append(tem)
        answer.append(tem_row)
    return answer


solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
