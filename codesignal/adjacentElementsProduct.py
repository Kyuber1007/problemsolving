def solution(inputArray):
    tem = -999999  
    for i in range(len(inputArray) -1 ):
        if tem < inputArray[i] * inputArray[i+1]:
            tem = inputArray[i] * inputArray[i+1]
                        
    return tem
    
    # return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])