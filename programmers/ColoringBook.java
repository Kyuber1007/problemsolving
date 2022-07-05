import java.util.LinkedList;
import java.util.Queue;

class ColoringBook {
  public static void main(String[] args) {
    ColoringBook asdf = new ColoringBook();
    System.out.println(
        asdf.solution(6, 4,
            new int[][] { { 1, 1, 1, 0 }, { 1, 2, 2, 0 }, { 1, 0, 0, 1 }, { 0, 0, 0, 1 }, { 0, 0, 0, 3 },
                { 0, 0, 0, 3 } }));
  }

  public int[] solution(int m, int n, int[][] picture) {
    int numberOfArea = 0;
    int maxSizeOfOneArea = 0;
    boolean[][] visited = new boolean[m][n];

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (!visited[i][j] && picture[i][j] != 0) {
          maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(i, j, picture, visited, picture[i][j]));
          numberOfArea++;
        }
      }
    }

    int[] answer = new int[2];
    answer[0] = numberOfArea;
    answer[1] = maxSizeOfOneArea;
    System.out.println(answer[0]);
    System.out.println(answer[1]);
    return answer;
  }

  public int bfs(int cx, int cy, int[][] picture, boolean[][] visited, int color) {
    int[] dx = { 1, 0, -1, 0 };
    int[] dy = { 0, 1, 0, -1 };

    Queue<int[]> queue = new LinkedList<int[]>();
    queue.add(new int[] { cx, cy });
    int count = 1;

    visited[cx][cy] = true;

    while (!queue.isEmpty()) {
      int[] pull = queue.remove();
      int newX = pull[0];
      int newY = pull[1];

      for (int i = 0; i < 4; i++) {
        int nx = newX + dx[i];
        int ny = newY + dy[i];

        if (nx < 0 || nx >= visited.length || ny < 0 || ny >= visited[0].length) {
          continue;
        }
        if (visited[nx][ny] == false && (picture[nx][ny] == color)) {
          visited[nx][ny] = true;
          queue.add(new int[] { nx, ny });
          count++;
        }
      }
    }
    return count;
  }
}