def solution(input):
    inputs = input.split()
    inputs.sort()
    if inputs[0] == inputs[1] == inputs[2]:
        print (int(inputs[0]) * 1000 + 10000)
    elif inputs[0] == inputs[1] or inputs[1] == inputs[2]:
        print(int(inputs[1]) * 100 + 1000)
    else:
        print(int(inputs[2]) * 100)
  
solution("6 2 5")
