hour, minute, second = map(int, input().split())
time = int(input())

if second + time >= 60:
    min_plus = int((second + time) / 60)
    second = (second + time) % 60 
    minute = minute + min_plus

else:
    second = second + time

if minute >= 60:
    hour_plus = int((minute) / 60)
    minute = minute % 60
    hour = hour + hour_plus

if hour >= 24:
    hour = hour % 24

print(hour, minute, second)