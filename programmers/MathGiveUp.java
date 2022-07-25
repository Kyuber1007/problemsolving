import java.util.ArrayList;

class Solution {
  public int[] solution(int[] answers) {
    int[] first = { 1, 2, 3, 4, 5 };
    int[] second = { 2, 1, 2, 3, 2, 4, 2, 5 };
    int[] third = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

    int countFirst = 0, countSecond = 0, countThird = 0;
    ArrayList<Integer> tem = new ArrayList<Integer>(3);

    tem.add(0);
    tem.add(0);
    tem.add(0);

    for (int i = 0; i < answers.length; i++) {

      if (answers[i] == first[i % 5]) {
        tem.set(0, tem.get(0) + 1);
      }
      if (answers[i] == second[i % 8])
        tem.set(1, tem.get(1) + 1);
      if (answers[i] == third[i % 10])
        tem.set(2, tem.get(2) + 1);
    }

    int maxCount = Math.max(Math.max(tem.get(0), tem.get(1)), tem.get(2));
    int size = 0;
    for (int i = 0; i < tem.size(); i++) {
      if (maxCount == tem.get(i))
        size++;
    }

    int[] answer = new int[size];
    size = 0;
    for (int i = 0; i < tem.size(); i++) {
      if (maxCount == tem.get(i))
        answer[size++] = i + 1;
    }
    return answer;
  }
}