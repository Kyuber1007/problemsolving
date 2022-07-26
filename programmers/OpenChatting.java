import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Solution {
  ArrayList<String> answerList = new ArrayList<String>();
  Map<String, String> nameList = new HashMap<String, String>();

  public String[] solution(String[] record) {

    for (int i = 0; i < record.length; i++) {
      getOrder(record[i], nameList);
    }
    return changeFormat(answerList);
  }

  private String[] changeFormat(ArrayList<String> answerList) {
    String[] answer = new String[answerList.size()];
    for (int i = 0; i < answerList.size(); i++) {
      String[] tokens = answerList.get(i).split(",");
      if (tokens[0].equals("Enter"))
        answer[i] = nameList.get(tokens[1]) + "님이 들어왔습니다.";
      else if (tokens[0].equals("Leave")) {
        answer[i] = nameList.get(tokens[1]) + "님이 나갔습니다.";
      }
    }
    return answer;
  }

  public void getOrder(String msg, Map<String, String> nameList) {
    String[] token = msg.split(" ");
    int count = 0;
    if (!nameList.containsKey(token[1])) {
      count = 1;
      nameList.put(token[1], token[2]);
    }

    if (!token[0].equals("Change")) {
      if (token[0].equals("Enter") && count == 0) {
        if (!nameList.get(token[1]).equals(token[2]))
          nameList.replace(token[1], token[2]);
      }
      answerList.add(token[0] + "," + token[1]);
    } else {
      nameList.replace(token[1], token[2]);
    }
  }
}