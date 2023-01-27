def solution(s):
    arr = list(map(int, s.split()))
    arr.sort()
    
    return str(arr[0]) +  " " + str(arr[-1])
    
def solution2(s):
    arr = list(map(int, s.split()))
    return str(min(arr)) + " " + str(max(arr))
  
solution("-1 -2 -3 -4")
solution2("-1 -2 -3 -4")