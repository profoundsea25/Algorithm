import java.util.*;

public class Main {
    public static long[] arr = new long[100];
    public static void main(String[] args) {
        arr[1] = 1;
        arr[2] = 1;
        int n = 50;

        for (int i = 3; i < 50; i++) {
            arr[i] = arr[i-1] + arr[i-2];
        }
        System.out.println(arr[n]);
    }
}