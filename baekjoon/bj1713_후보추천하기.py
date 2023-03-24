import sys

input = sys.stdin.readline

N = int(input().strip())
recommendation_count = int(input().strip())
recommendations = list(map(int, input().split()))

timeline = []
pictures = {}

for recommendation in recommendations:
    if pictures.get(recommendation, False):
        pictures[recommendation] += 1
    else:
        pictures[recommendation] = 1  
        timeline.append(recommendation)
    
    if len(pictures) > N:
        min_value = 1001
        delete_key = -1
        delete_index = -1
        # min_value = min(pictures.values())
        for i in range(len(timeline) - 2, -1, -1):
            key = timeline[i]
            if pictures[key] <= min_value:
                min_value = pictures[key]
                delete_key = key
                delete_index = i
        pictures.pop(delete_key)              
        timeline.pop(delete_index)
        
print(*sorted(pictures.keys()))