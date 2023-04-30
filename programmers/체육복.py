  def solution(n, lost, reserve):
      answer = 0
      
      cur_status = [1] * n
      
      for _ in reserve:
          cur_status[_ - 1] += 1
          
      for _ in lost:
          cur_status[_ - 1] -= 1
          
      for i in range(n):
          if cur_status[i] == 0:
              if i - 1 >= 0:
                  if cur_status[i - 1] > 1:
                      cur_status[i-1] -= 1
                      cur_status[i] += 1
                      continue
              if i + 1 < n:
                  if cur_status[i + 1] > 1:
                      cur_status[i + 1] -= 1
                      cur_status[i] += 1
      for i in cur_status:
          if i > 0:
              answer += 1
      return answer