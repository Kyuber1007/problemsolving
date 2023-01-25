def solution(inputArray):
    number = 0
    for i in range(len(inputArray)-1):
        tem1 = inputArray[i] + 1
        tem2 = inputArray[i+1]
        if tem2 < tem1:
           number += tem1 - tem2 
           inputArray[i + 1] = tem1
    return number