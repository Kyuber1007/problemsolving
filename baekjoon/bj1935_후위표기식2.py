import collections
n = int(input())
string = list(input())
string_length = len(string)

digits = []
for i in range(n):
    digits.append(int(input()))

operands = collections.deque([])

result = 0
for i in range(string_length):
    tem = string[i]
    if tem.isalpha():
        operands.append(digits[ord(string[i]) - ord('A')])
    else:
        b = operands.pop()
        a = operands.pop()
        if tem == '+':
            operands.append(a + b)
        elif tem == '-':
            operands.append(a - b)
        elif tem == '*':
            operands.append(a * b)
        elif tem == '/':
            operands.append(a / b)
result = operands.pop()
print(f"{result:.2f}")
