import java.util.PriorityQueue;

class Solution {
  public int solution(int[] scoville, int K) {
    int answer = 0;

    PriorityQueue<Integer> queue = new PriorityQueue<Integer>(scoville.length);
    for (int tem : scoville) {
      queue.offer(tem);
    }
    while (queue.peek() <= K) {
      if (queue.size() == 1) {
        return -1;
      }
      int newFood = queue.poll() + queue.poll() * 2;
      queue.offer(newFood);
      answer++;
    }
    return answer;
  }
}