class Solution {
  public long solution(int w, int h) {
    long num = ((w > h) ? (long) Math.ceil(w / h) * h : (long) Math.ceil(h / w) * w);
    System.out.println(w + ", " + h);
    if (w > h) {
      double tem;
      tem = Math.ceil(w / h);
      System.out.println(tem);
    } else {
      System.out.println(h / w);
      double tem = Math.ceil(h / w);
      System.out.println(tem);
    }
    System.out.println(num);
    System.out.println(w * h - num);
    return w * h - num;
  }
}