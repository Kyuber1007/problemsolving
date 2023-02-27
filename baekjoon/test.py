# print('A')
# print(ord('A') - 65)


from heapq import heappop, heappush

int_list = []

heappush(int_list, (1, 'test'))
heappush(int_list, (2, 'test2'))
heappush(int_list, (6, 'test3'))
heappush(int_list, (10, 'test4'))
heappush(int_list, (7, 'test5')) 
print(int_list)

print(int_list[3][1])
print(heappop(int_list))