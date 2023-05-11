# def solution(a, b):
#     answer = ''
#     tem = 0
#     day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
#     for i in range(1, a):
#         if i < 8:
#             if i % 2 == 1:
#                 tem += 31
#             if i % 2 == 0:
#                 if i == 2:
#                     tem += 29
#                 else:
#                     tem += 30
#         else:
#             if i % 2 == 0:
#                 tem += 31
#             else:
#                 tem += 30
#     tem += b
#     tem -= 1
#     tem %= 7
    
#     return day[tem]

def solution(a, b):
    answer = ''
    tem = 0
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(1, a):
        tem += months[i]
    tem += b - 1
    tem %= 7
    
    return day[tem]