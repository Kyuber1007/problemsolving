def solution(a):
    result = [];
    for i in range(len(a)):
        if(a[i] != -1):
            result.append(a[i]);
    result.sort()
    tem = 0;
    for i in range(len(a)):
        if(a[i] != -1):
            a[i] = result[tem]
            tem += 1        
    return a
