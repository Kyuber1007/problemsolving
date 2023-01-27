# def solution(participant, completion):
#   answer = ''
#   for i in range(len(completion)):
#     for j in range(len(participant)):
#       if(participant[j] == completion[i]):
#         participant.remove(participant[j])
#         break
#   print(participant[0])
#   return participant[0]


from collections import Counter

def solution(participant, completion):
  i = Counter(participant) - Counter(completion)
  return print(list(i.keys())[0])


solution(["leo", "kiki", "eden"],["leo", "kiki"])