class Solution {
  public int solution(int[] numbers) {
    int answer = 45;

    for (int i : numbers) {
      answer -= i;
    }
    return answer;

    /*
     * int answer = -1;
     * int[] checkNum = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
     * for (int i = 0; i < numbers.length; i++) {
     * checkNum[numbers[i]] = 1;
     * }
     * for (int i = 0; i < checkNum.length; i++) {
     * if (checkNum[i] == 0)
     * answer += i;
     * }
     * return answer;
     */
  }
}