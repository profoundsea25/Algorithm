import java.util.*;

public class Main {
    public static final int INF = 999999999;

    // 2차원 리스트를 이용해 인접 행렬 표현;
    public static int[][] graph = {
        {0, 7, 5},
        {7, 0, INF},
        {5, INF, 0}
    };

    public static void main(String[] args) {
        for(int i = 0; i <  3; i++) {
            for (int j = 0; j < 3; j++){
                // print와 println의 차이점 : print는 출력 후 \n을 하지 않는다.
                System.out.print(graph[i][j] + " ");
            }
            // 줄바꿈
            System.out.println();
        }
    }
}