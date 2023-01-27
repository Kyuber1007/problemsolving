from time import time 

def solution(image):
    now1= time()
    width = len(image) 
    length = len(image[0]) - 2
    
    new_rec = [[0 for col in range(width)] for raw in range(length)]
   
    for i in range(len(image)):
        for j in range(len(image[i]) - 2):
            new_rec[j][i] = (image[i][j] + image[i][j + 1] + image[i][j + 2]) / 3 

    width = len(new_rec)
    length = len(new_rec[0]) - 2
    final_rec = [[0 for col in range(width)] for raw in range(length)]

    for i in range(len(new_rec)):
        for j in range(len(new_rec[i]) - 2):
            final_rec[j][i] = int((new_rec[i][j] + new_rec[i][j + 1] + new_rec[i][j + 2]) / 3)

    time_diff = time() - now1
    print(f'{time_diff:f}') 
    return final_rec
  
  