import java.util.*;

public class Main {
    public static int[] dp = new int[101];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = sc.nextInt();
        }

        dp[0] = data[0];
        dp[1] = Math.max(data[0], data[1]);
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + data[i]);
        }

        System.out.println(dp[n-1]);
    }
}