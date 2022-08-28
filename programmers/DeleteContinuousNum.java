import java.util.ArrayList;

public class Solution {
  public int[] solution(int[] arr) {
    ArrayList<Integer> tem = new ArrayList<>();
    int i = 0;
    while (i < arr.length - 1) {
      if (arr[i] == arr[i + 1]) {
        i++;
      } else {
        i++;
        tem.add(arr[i]);
      }
    }
    tem.add(arr[arr.length - 1]);

    int[] answer = new int[tem.size()];
    for (int j = 0; j < answer.length; j++) {
      answer[j] = tem.get(j);
    }
    return answer;
  }
}