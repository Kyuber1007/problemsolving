import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

class Solution {
  public int[] solution(String[] id_list, String[] report, int k) {
    int[] answer = new int[id_list.length];
    int[][] relation = new int[id_list.length][id_list.length];
    int[] reportedNum = new int[id_list.length];

    HashSet<String> reportList = new HashSet<>(Arrays.asList(report));
    ArrayList<String> id_listList = new ArrayList<>(Arrays.asList(id_list));

    for (String tem : reportList) {
      String[] reported = tem.split(" ");
      relation[id_listList.indexOf(reported[0])][id_listList.indexOf(reported[1])] = 1;
      reportedNum[id_listList.indexOf(reported[1])] += 1;
    }
    for (int i = 0; i < reportedNum.length; i++) {
      if (reportedNum[i] >= k) {
        for (int j = 0; j < id_list.length; j++) {
          if (relation[j][i] == 1) {
            answer[j] += 1;
          }
        }
      }
    }
    return answer;
  }
}