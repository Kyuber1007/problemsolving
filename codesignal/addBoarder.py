def solution(picture):
    result = []
    tem =""
    length = len(picture[0]) + 2

    for i, s in enumerate(picture):
        picture[i] = "*" + s + "*" 
    
    
    return ["*" * length] + picture +  ["*" * length]