class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int count = 0;
        int zeros = 0;
        for (int i = 0; i < 6; i++) {
            int num = lottos[i];
            if (num == 0)
                zeros++;
            for (int j = 0; j < 6; j++) {
                if (num == win_nums[j]) {
                    count++;
                }
            }
        }
        int[] answer = { count, count + zeros };
        answer[1] = 7 - count == 7 ? 6 : 7 - count;
        answer[0] = 7 - (count + zeros) == 7 ? 6 : 7 - (count + zeros);
        return answer;
    }
}