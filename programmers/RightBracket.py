def solution(s):
  right = 0
  left = 0
  for i in range(len(s)):
    if(right > left):
      return False
    if s[i] == '(':
      left += 1
    elif s[i] == ')':
      right += 1
  
  if left !=  right:
    return False
  return True
    