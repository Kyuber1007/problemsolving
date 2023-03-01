from heapq import heappop, heappush
import sys

input = sys.stdin.readline
test_num = int(input())

# case의 갯수에 따라서 진행
for i in range(test_num):
    operations_num = int(input())
    max_heap = []
    min_heap = []
    exist = []
    
    # operations의 갯수에 따라서 진행
    for j in range(operations_num):
        # operation을 입력 받음
        operation = input().strip().split()
       
        # insert operation일 경우
        if operation[0] == 'I':
            heappush(max_heap, int(operation[1]))
            
        # delete operation일 경우
        else:
            if len(int_list) > 0:
                if operation[1] == '-1':
                    heappop(int_list)
                else:
                    pop_value = heappop(int_list)
                    heappush(int_list, pop_value)
                    int_list.pop()
        print(int_list)
    if len(int_list) == 0:
        print("EMPTY")
    else:
        pop_value = heappop(int_list)
        heappush(int_list, pop_value)
        if len(int_list) > 1:
            print(int_list[-1], pop_value)
        else:
            print(pop_value, pop_value)
