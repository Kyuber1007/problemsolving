import java.util.LinkedList;
import java.util.Queue;

class Solution {
  public int solution(int[] queue1, int[] queue2) {
    long sum1 = 0;
    long sum2 = 0;
    int midVal = 0;
    Queue<Long> first = new LinkedList<Long>();
    Queue<Long> second = new LinkedList<Long>();
    int cnt = 0;
    for (int i = 0; i < queue1.length; i++) {
      sum1 += queue1[i];
      first.offer((long) queue1[i]);
    }
    for (int i = 0; i < queue2.length; i++) {
      sum2 += queue2[i];
      second.offer((long) queue2[i]);
    }

    if ((sum1 + sum2) % 2 != 0)
      return -1;

    while (true) {
      if (sum1 > sum2) {
        long tem = first.poll();
        sum1 -= tem;
        sum2 += tem;
        second.offer(tem);
        cnt++;
      } else if (sum1 < sum2) {
        long tem = second.poll();
        sum2 -= tem;
        sum1 += tem;
        first.offer(tem);
        cnt++;
      } else if (sum1 == sum2) {
        System.out.println(cnt);
        return cnt;
      }

      if (cnt > (queue1.length + queue2.length) * 2)
        return -1;
    }
  }
}