import java.util.*;

public class Main {
    // 반복적으로 구현한 n!
    public static int factorialIterative(int n) {
        int result = 1;

        for (int i = 0; i < n; i++) {
            result *= i;
        }

        System.out.println(result);
    }

    public static int factorialRecursive(int n) {
        if (n <= 1) return 1;
        return n * factorialIterative(n-1);
    }

    public static void main(String[] args) {
        System.out.println(factorialIterative(5));
        System.out.println(factorialRecursive(5));
    }
}