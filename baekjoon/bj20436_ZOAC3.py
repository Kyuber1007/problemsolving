import sys
input = sys.stdin.readline

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
left_hand_char = 'qwertasdfgzxcv'


def find_index(character):
    for i in range(len(keyboard)):
        if character in keyboard[i]:
            return i, keyboard[i].index(character)


left, right = map(str, input().split())

right_x, right_y = find_index(right)
left_x, left_y = find_index(left)
in_str = list(map(str, input().strip()))
count = 0

for char in in_str:
    count += 1
    x, y = find_index(char)
    if char in left_hand_char:
        count += abs(x - left_x) + abs(y - left_y)
        left_x, left_y = x, y
    else:
        count += abs(x-right_x)+abs(y-right_y)
        right_x, right_y = x, y

print(count)
