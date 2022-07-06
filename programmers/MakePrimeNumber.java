class MakePrimeNumber {
  public static void main(String[] args) {
    int[] nums = { 1, 2, 3, 4 };
    int[] nums1 = { 1, 2, 7, 6, 4 };

    MakePrimeNumber solution = new MakePrimeNumber();
    System.out.println(solution.solution(nums));
    System.out.println(solution.solution(nums1));
  }

  public int solution(int[] nums) {
    int answer = 0;
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        for (int k = j + 1; k < nums.length; k++) {
          int tem = nums[i] + nums[j] + nums[k];
          answer = answer + checkPrimeOrNot(tem, answer);
        }
      }
    }
    return answer;
  }

  public int checkPrimeOrNot(int tem, int answer) {
    int count = 0;
    for (int i = 2; i <= (int) Math.sqrt(tem); i++) {
      if (tem % i == 0) {
        count++;
      }
    }
    if (count == 0) {
      return 1;
    } else
      return 0;
  }
}