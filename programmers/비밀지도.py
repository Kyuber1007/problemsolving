def solution(n, arr1, arr2):
    answer = []
    def 해독(arr):
        result_arr = []
        for i in range(n):
            tem = arr[i]
            result = ''
            
            while tem > 0:
                tem1 = tem // 2
                tem2 = tem % 2
                tem = tem1
                result += str(tem2)
            result_arr.append(result[::-1].zfill(n))
        return result_arr

    해독1 = 해독(arr1)
    해독2 = 해독(arr2)
    result = []
    for i in range(n):
        line = ''
        for j in range(n):
            if 해독1[i][j] == '1' or 해독2[i][j] == '1':
                line+="#"
            else:
                line += " "
        result.append(line)
    return result