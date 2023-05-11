from collections import defaultdict

def solution(fees, records):
    answer = []
    
    in_ = {}
    total_parked_time = defaultdict(int)
    
    def calculate_fee(time):
        if time <= fees[0]:
            return fees[1]
        else:
            if (time - fees[0]) % fees[2] == 0:
                return fees[1] + fees[3] * ((time - fees[0]) // fees[2])
            else:
                return fees[1] + fees[3] * ((time - fees[0]) // fees[2] + 1)
    for i in range(len(records)):
        tem = records[i].split(" ")
        
        if tem[2] == 'IN':
            _ = list(map(int, tem[0].split(':')))
            in_[tem[1]] =  _[0] * 60 + _[1]
            
        elif tem[2] == 'OUT':
            in_time = in_[tem[1]]
            _ = list(map(int, tem[0].split(':')))
            out_time = _[0] * 60 + _[1]
            total_time = out_time - in_time
            total_parked_time[tem[1]] += total_time
            in_.pop(tem[1])
            
    while in_:
        _ = list(in_.keys())
        in_time = in_[_[0]]
        total_time = 60*23 + 59 - in_time
        total_parked_time[_[0]] += total_time
        in_.pop(_[0])
        
    tem = list(total_parked_time.items())
    tem.sort(key=lambda x: x[0])

    for i in range(len(tem)):
        answer.append(calculate_fee(tem[i][1]))
    return answer