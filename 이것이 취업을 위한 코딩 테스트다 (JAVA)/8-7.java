import java.util.*;

public class Main {
    public static int[] dp = new int[1001];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();

        dp[0] = 1;
        dp[1] = 3;
        for (int i = 2; i < n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]*2) % 796796;
        }
        System.out.println(dp[n-1]);
    }
}