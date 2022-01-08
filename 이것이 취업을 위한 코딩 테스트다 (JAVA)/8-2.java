import java.util.*;

public class Main {
    public static long[] arr = new long[100];

    public static long fibo(int x) {
        if (x == 1 || x == 2) {
            return 1;
        }

        if (arr[x] != 0) {
            return arr[x];
        }
        
        arr[x] = fibo(x-1) + fibo(x-2);
        return arr[x];
    }

    public static void main(String[] args) {
        System.out.println(fibo(50));
    }
}