class Solution {
  int leftRow = 3;
  int leftCol = 0;
  int rightRow = 3;
  int rightCol = 2;
  int leftDist = 0;
  int rightDist = 0;
  String answer = "";

  int row = 0;
  int col = 0;

  public String solution(int[] numbers, String hand) {

    for (int i = 0; i < numbers.length; i++) {
      if (numbers[i] == 0) {
        row = 3;
        col = 1;
      } else {
        row = (numbers[i] - 1) / 3;
        col = (numbers[i] - 1) % 3;
      }
      if (col == 0) {
        answerLeft();

      } else if (col == 2) {
        answerRight();

      } else {
        rightDist = Math.abs(col - rightCol) + Math.abs(row - rightRow);
        leftDist = Math.abs(col - leftCol) + Math.abs(row - leftRow);
        if (leftDist == rightDist) {
          if (hand.equals("right")) {
            answerRight();
          } else {
            answerLeft();
          }
        } else if (leftDist < rightDist) {
          answerLeft();
        } else {
          answerRight();
        }
      }
    }
    return answer;
  }

  private void answerRight() {
    answer += "R";
    rightCol = col;
    rightRow = row;
  }

  private void answerLeft() {
    answer += "L";
    leftRow = row;
    leftCol = col;
  }
}