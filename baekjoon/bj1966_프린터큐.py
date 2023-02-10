n = int(input())


def get_order(num_of_files, target, priorities):
    count = 0
    target_priority = priorities[target]

    max_priority = max(priorities)
    priorities[target] = -1

    while True:
        max_priority = max(priorities)
        if max_priority > target_priority:
            max_index = priorities.index(max_priority)
            priorities = priorities[max_index+1:] + priorities[:max_index]
            count += 1
        elif max_priority == target_priority:
            if priorities.index(-1) < priorities.index(max_priority):
                return count + 1
            else:
                max_index = priorities.index(max_priority)
                priorities = priorities[max_index+1:] + priorities[:max_index]
                count += 1
        else:
            return count + 1


for i in range(n):
    num_of_files, target = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(get_order(num_of_files, target, priorities))
