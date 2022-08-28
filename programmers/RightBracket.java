class Solution {
  boolean solution(String s) {
    boolean answer = true;
    int left = 0;
    int right = 0;

    for (int i = 0; i < s.length(); i++) {
      if (right > left)
        return false;
      if (s.charAt(i) == '(')
        left++;
      else if (s.charAt(i) == ')') {
        right++;
      }
    }
    if (right != left)
      return false;
    return answer;
  }
}