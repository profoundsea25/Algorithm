import java.util.*;

public class Main {
    // 집합 자료형 (HashSet) 이용
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        HashSet<Integer> s = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            s.add(x);
        }

        int m = sc.nextInt();
        for (int i = 0; i < m; i++) {
            int target = sc.nextInt();

            if (s.contains(target)) {
                System.out.print("yes ");
            }
            else {
                System.out.print("no ");
            }
        }
    }
}