hour, minute = map(int, input().split())
time = int(input())

if minute + time >= 60:
    hour_plus = int((minute + time) / 60)
    minute = (minute + time) % 60
    hour = hour + hour_plus


else:
    minute = minute + time

if hour >= 24:
    hour = hour % 24

print(hour, minute)