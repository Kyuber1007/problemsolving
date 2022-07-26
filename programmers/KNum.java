import java.util.Arrays;

class Solution {
  public int[] solution(int[] array, int[][] commands) {
    int[] answer = new int[commands.length];
    System.out.println(answer.length);

    for (int i = 0; i < commands.length; i++) {
      int size = commands[i][1] - commands[i][0] + 1;
      int[] tem = new int[size];
      for (int j = 0; j < size; j++) {
        tem[j] = array[commands[i][0] - 1 + j];
      }
      Arrays.sort(tem);
      answer[i] = tem[commands[i][2] - 1];
    }

    return answer;
  }
}