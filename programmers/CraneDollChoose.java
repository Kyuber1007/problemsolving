import java.util.ArrayList;

class Solution {
  public int solution(int[][] board, int[] moves) {
    int answer = 0;
    int count;
    ArrayList<Integer> bucket = new ArrayList<>();

    for (int i = 0; i < moves.length; i++) {
      count = 0;
      int move = moves[i] - 1;
      int j = 0;
      while (board[j][move] == 0) {
        count = 0;
        j++;
        if (j == board[move].length) {
          count = 1;
          break;
        }
      }
      if (count == 0) {
        bucket.add(board[j][move]);
        board[j][move] = 0;
      }
      if (bucket.size() >= 2) {
        if (bucket.get(bucket.size() - 1).equals(bucket.get(bucket.size() - 2))) {
          answer += 2;
          bucket.remove(bucket.size() - 1);
          bucket.remove(bucket.size() - 1);
          if (bucket.size() >= 2)
            answer = checkBucketAgain(bucket, answer);
        }
      }
    }
    return answer;
  }

  public int checkBucketAgain(ArrayList<Integer> bucket, int answer) {
    for (int i = 1; i < bucket.size(); i++) {
      if (bucket.get(i) == bucket.get(i - 1)) {
        answer += 2;
        bucket.remove(i - 1);
        bucket.remove(i - 1);
      }
    }
    return answer;
  }
}