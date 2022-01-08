import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] money = new int[n];
        for (int i = 0; i < n; i++) {
            money[i] = sc.nextInt();
        }

        int[] dp = new int[m+1];
        Arrays.fill(dp, 10001);

        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = money[1]; j <= m; j++) {
                if (dp[j - money[i]] != 10001) {
                    dp[j] = Math.min(dp[j], dp[j - money[i]] + 1);
                }
            }
        }

        if (d[m] == 10001) {
            System.out.println(-1);
        }
        else {
            System.out.println(dp[m]);
        }
    }
}