import java.util.*;

public class Main {
    // 계수 정렬 이용
    public static int[] arr = new int[1000001];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int data = sc.nextInt();
            arr[data] += 1;
        }

        int m = sc.nextInt();
        for (int i = 0; i < m; i++) {
            int target = sc.nextInt();
            if (arr[target] != 0) {
                System.out.print("yes ");
            }
            else {
                System.out.print("no ");
            }
        }
    }
}