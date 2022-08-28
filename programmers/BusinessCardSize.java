class Solution {
  public int solution(int[][] sizes) {
    int max = 0;
    for (int i = 0; i < sizes.length; i++) {
      if (max < sizes[i][0]) {
        max = sizes[i][0];
      } else if (max < sizes[i][1]) {
        max = sizes[i][1];
      }
    }
    int h = 0;
    for (int i = 0; i < sizes.length; i++) {
      int tem;
      tem = (sizes[i][0] > sizes[i][1]) ? sizes[i][1] : sizes[i][0];
      if (h < tem)
        h = tem;
    }
    return max * h;
  }
}