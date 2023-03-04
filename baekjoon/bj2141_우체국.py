import sys
input = sys.stdin.readline

N = int(input().strip())
villages = []

total_people = 0
for i in range(N):
    new_village = list(map(int, input().split()))
    villages.append(new_village)
    total_people += new_village[1]

villages.sort()
print(max(villages, key=lambda x: x[1]))


count = 0
for i in range(N):
    count += villages[i][1]
    # 중간 값을 구하면 최소 거리가 됨.
    if count >= total_people/2:
        print(villages[i][0])
        break

# min = -1
# min_place = 0


# for i in range(N):
#     tem_place = villages[i][0]
#     tem_distance = 0

#     for j in range(N):
#         if j > i:
#             tem_distance += (villages[j][0] - tem_place) * villages[j][1]
#         else:
#             tem_distance += (tem_place - villages[j][0]) * villages[j][1]
#     if min < 0:
#         min_place = tem_place
#         min = tem_distance
#     if min > tem_distance:
#         min = tem_distance
#         min_place = tem_place

# print(min_place)
