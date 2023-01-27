from queue import Queue

def solution(queue1, queue2):
  que1 = Queue()
  que2 = Queue()
  
  sum1 = 0
  sum2 = 0
  for i in range(len(queue1)):
    sum1 += queue1[i]
    que1.put(queue1[i])
  for i in range(len(queue2)):
    sum2 += queue2[i]
    que2.put(queue2[i])
    
  if((sum1 + sum2) % 2) != 0:
    return -1
  
  cnt = 0
  while(True):
    if sum1 > sum2:
      tem = que1.get()
      sum1 -= tem
      sum2 += tem
      que2.put(tem)
      cnt += 1
    elif sum1 <sum2:
      tem = que2.get()
      sum1 += tem
      sum2 -= tem
      que1.put(tem)
      cnt += 1
    elif sum1 == sum2:
      return cnt
    if cnt > (len(queue1)  + len(queue2)) * 2: 
      return -1