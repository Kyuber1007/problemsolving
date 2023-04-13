def solution(n, t, m, timetable):
    answer = 24 * 60
    
    timetable_int = []
    for time in timetable:
        hour, time = map(int, time.split(':'))
        timetable_int.append(hour*60 + time)
    timetable_int.sort()
    
    j = 0
    for i in range(n):
        depart_time = 9 * 60 + t * i
        cnt = 0
        while cnt < m and  j < len(timetable_int) and timetable_int[j] <= depart_time :
            j += 1
            cnt += 1
        if cnt < m:
            answer = depart_time
        else:
            answer = timetable_int[j-1] -1
    print(answer//60, answer%60)
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

# solution(10, 60 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	)
# solution(1,1, 1,["23:59"]	 )
# solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]	)
# solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]	)
# solution(2, 10, 2, ["09:10", "09:09", "08:00"]	)
solution(1, 1,5, ["08:00", "08:01", "08:02", "08:03"])