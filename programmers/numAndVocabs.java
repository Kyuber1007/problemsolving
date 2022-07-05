class Solution {

  public int solution(String s) {
    String[] words = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

    for (int i = 0; i < words.length; i++) {
      String tem = words[i];
      s = s.replace(tem, String.valueOf(i));
    }
    return Integer.parseInt(s);
  }
}
